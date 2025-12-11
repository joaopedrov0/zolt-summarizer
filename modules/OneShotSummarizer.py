from modules.ArcanaFlow import Nayahath
from modules.Interfaces import SummarizerInterface
import ollama

class OneShotSummarizer(SummarizerInterface):
    def __init__(self, model, prompt="Você é um especialista em resumo de reuniões envolvendo múltiplos falantes."):
        self.model = model
        self.prompt = prompt
    
    def summarize(self, content):
        
        Nayahath.action("Summarizer", "Iniciando resumo one-shot.")
            
        res: ollama.ChatResponse = ollama.chat(
            model=self.model,
            messages=[
                {"role": "system", "content": self.prompt},
                {"role": "system", "content": "Mantenha os nomes dos 'SPEAKER_XX' exatamente como aparecem nos textos."},
                {"role": "user", "content": "Crie um resumo conciso do seguinte conteúdo de transcrição de reunião:"},
                {"role": "user", "content": content}
            ]
        )
        
        return res.message.content
        

    def setPrompt(self, prompt):
        self.prompt = prompt
