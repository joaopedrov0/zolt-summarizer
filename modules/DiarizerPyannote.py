from modules.ArcanaFlow import Nayahath
from modules.Interfaces import DiarizerInterface

import torch
from pyannote.audio import Pipeline
from pyannote.audio.pipelines.utils.hook import ProgressHook

import pyannote.audio.core.task
torch.serialization.add_safe_globals([pyannote.audio.core.task.Specifications])
torch.serialization.add_safe_globals([pyannote.audio.core.task.Problem])
torch.serialization.add_safe_globals([pyannote.audio.core.task.Resolution])

class DiarizerPyannote(DiarizerInterface):
    def diarize(self, filepath, hugging_face_token: str, model_checkpoint="pyannote/speaker-diarization-community-1", device="cpu"):
        
        Nayahath.warning("Diarizer", "Importações acontecendo dentro do método")
        
        Nayahath.action("Diarizer", f"Loading model using token {hugging_face_token}")
        
        pipeline = Pipeline.from_pretrained(model_checkpoint, token=hugging_face_token)
        
        Nayahath.action("Diarizer", f"Model loaded passing pipeline to device '{device}'")
        
        pipeline.to(torch.device(device))
        
        with ProgressHook() as hook:
            output = pipeline(filepath, hook=hook)
            
        diarization = []
        
        Nayahath.action("Diarizer", "Diarization completed. Grouping results.")
        
        for turn, speaker in output.speaker_diarization:
            diarization.append({
                "speaker": speaker,
                "start": turn.start,
                "stop": turn.end
            })
            
        Nayahath.action("Diarizer", "Results grouped.")
        
        return diarization