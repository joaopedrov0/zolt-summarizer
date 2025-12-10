from abc import ABC, abstractmethod
from pathlib import Path

class DiarizerInterface(ABC):
    @abstractmethod
    def diarize(self, filepath: Path) -> list:
        """
        input: filepath:Path
        output: dict(speaker:str, start:float, stop:float)[]
        """
        pass