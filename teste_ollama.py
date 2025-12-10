from modules.SummarizerQwen3 import SummarizerQwen3
from modules import OutputManager

text = '''Cole um texto aqui para ser resumido pelo modelo'''
from modules.ArcanaFlow import Nayahath

Nayahath.add_entity("Summarizer", "yellow")

Nayahath.action("Summarizer", "Initializing Summarization")

om = OutputManager('./teste_ollama')
om.create_timestamped_folder("TESTE_QWEN_PERGUNTAS")

qwen = SummarizerQwen3(model="llama3")
    
res = qwen.summarize(text)

om.save_text_file("OUTPUT", res)

# SPEAKERS_LIST = ["SPEAKER_00", "SPEAKER_01", "SPEAKER_02", "SPEAKER_03"]
# counter = 0
# for s in SPEAKERS_LIST:
#     question = qwen.questionToSpeaker(s, context=textABC)
#     om.save_text_file(f"{s}_question", question)
#     counter += 1
#     Nayahath.action("Summarizer", f"Pergunta concluída {counter}/{len(SPEAKERS_LIST)}")