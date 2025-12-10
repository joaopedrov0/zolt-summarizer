from modules.ArcanaFlow import Nayahath
from modules.Interfaces import TranscripterInterface

class TranscripterWhisper(TranscripterInterface):
    def transcript(self, filepath, model="turbo", prompt=""):
        
        import whisper
        
        Nayahath.warning("Transcripter", "Importações acontecendo dentro do método")
        
        Nayahath.action("Transcripter", f"Loading transcription model. Model selected: {model}. Using prompt? {prompt != ""}")
        
        model = whisper.load_model("turbo")
        
        Nayahath.action("Transcripter", f"Model loaded, initializing transcription...")
        
        result = model.transcribe(audio=str(filepath), initial_prompt=prompt, carry_initial_prompt=prompt!="")
        
        Nayahath.action("Transcripter", f"Transcription completed. Grouping results...")
        
        transcription_segments = []
        
        for r in result["segments"]:
            transcription_segments.append({
                "text": r["text"],
                "start": r["start"],
                "stop": r["end"]
            })
            
        Nayahath.action("Transcripter", "Results grouped")
        
        return transcription_segments
        