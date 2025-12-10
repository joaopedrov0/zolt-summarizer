from abc import ABC, abstractmethod

class SummarizerInterface(ABC):
    @abstractmethod
    def summarize(self, content: str) -> str:
        """
        input: content: str
        output: str
        """
        pass
    
    @abstractmethod
    def setPrompt(self, prompt: str) -> None:
        """
        Defines the prompt used in summary
        """
        pass