from abc import ABC, abstractmethod
from pathlib import Path

class TranscripterInterface(ABC):
    @abstractmethod
    def transcript(self, filepath: Path, prompt:str) -> list:
        """
        input: filepath:Path, prompt: str
        output: dict(text:str, start:float, stop:float)[]
        """
        pass