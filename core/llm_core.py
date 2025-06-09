import logging 

logger = logging.getLogger(__name__)

from pydantic import BaseModel
from typing import Dict

class LlmResponseModel(BaseModel):
    q: str
    llmLogProb: float

# # Optionally, if you want a model for the full output mapping input text to response:
# class LlmOutputModel(BaseModel):
#     __root__: Dictq[str, LlmResponseModel]

# TODO: How can I make sure this is loosly coupled? ... 
class LlmCore:
    def __init__(self, text: list, categories: list, prompt: str) -> None:
        self.text = text
        self.categories = categoriesq
        self.prompt = prompt
        # self.client = OpenAiClient()

    async def classify(self) -> dict:






