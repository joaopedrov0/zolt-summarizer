from modules.ArcanaFlow import Nayahath
from modules.Interfaces import SummarizerInterface
import ollama

class SummarizerQwen3(SummarizerInterface):
    def __init__(self, model, prompt="Você é um especialista em resumo de reuniões envolvendo múltiplos falantes.", block_size=10):
        self.model = model
        self.prompt = prompt
        self.block_size = block_size
        self.context = ""
    
    def summarize(self, content):
        
        # Nayahath.warning("Summarizer", "Importações acontecendo dentro do método")
        
        blocks = self.getBlocks(content)
        
        res = []
        
        # context = "Nenhum contexto ainda, primeiro bloco de texto."
        
        for block in blocks:
            res.append(self.summarizeBlock("\n".join(block)))
            if(self.context == ""):
                self.context = res[0]
            else:
                self.context = self.updateContext("\n".join(block))
            Nayahath.action("Summarizer", f"Bloco {len(res)}/{len(blocks)} processado.")
            
        return "\n".join(res) + "\nContexto final:\n" + self.context
        
    def summarizeBlock(self, block):
        res: ollama.ChatResponse = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": "Não inclua na resposta nenhuma palavra que não foi pedida na pergunta."},
                {"role": "system", "content": self.prompt},
                {"role": "system", "content": f"Faça um resumo deste trecho de transcrição considerando este contexto: {self.context}"},
                {"role": "system", "content": "Mantenha os nomes dos 'SPEAKER_XX' exatamente como aparecem nos textos."},
                {"role": "user", "content": block}
            ]
        )
        
        return res.message.content
        
    def getBlocks(self, content):
        
        block_size = self.block_size
        
        raw = content.split("\n")
        
        blocks_num = len(raw) // block_size
        
        blocks = []
        
        for i in range(blocks_num):
            new_block = []
            for j in range(block_size):
                if (len(raw)==0):
                    break
                new_block.append(raw[0])
                del raw[0]
            blocks.append(new_block)
        
        return blocks
    
    def setPrompt(self, prompt):
        self.prompt = prompt
        
    def questionToSpeaker(self, speaker, context):
        """
        Esse método retorna uma pergunta com o objetivo de mapear os speakers com nomes
        """
        
        res: ollama.ChatResponse = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": "Não inclua na resposta nada que não foi pedido na pergunta."},
                # {"role": "system", "content": "Seu objetivo é unicamente responder com uma pergunta, não resuma o texto enviado, e não inclua nenhuma palavra que não faça parte da pergunta que foi pedida."},
                {"role": "system", "content": f"Responda a pergunta levando esse contexto em consideração: {context}"},
                # {"role": "user", "content": f"Seu objetivo é formular uma pergunta para identificar o speaker {speaker}, abordando na pergunta algo que foi falado por ele."},
                {"role": "user", "content": f"Qual o papel do falante {speaker} nessa conversa?"},
            ]
        )
        
        return res.message.content

    def updateContext(self, content):
        
        Nayahath.action("Summarizer", "Atualizando contexto.")
        res: ollama.ChatResponse = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": "Não inclua na resposta nenhuma palavra que não foi pedida na pergunta."},
                {"role": "system", "content": self.prompt},
                {"role": "system", "content": f"Contexto: {self.context}"},
                {"role": "user", "content": f"Atualize o contexto com base neste novo trecho da conversa: {content}"}
            ]
        )
        print(res.message.content)
        Nayahath.action("Summarizer", "Contexto atualizado.")
        return res.message.content
