from abc import ABC, abstractmethod

class AbstractClassifyClient(ABC):
    @abstractmethod
    async def classify(self) -> dict:
        pass


