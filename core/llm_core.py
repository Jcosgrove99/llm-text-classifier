import logging 

logger = logging.getLogger(__name__)

from pydantic import BaseModel
from typing import Dict

class LlmResponseModel(BaseModel):
    llmCategory: str
    llmLogProb: float

# # Optionally, if you want a model for the full output mapping input text to response:
# class LlmOutputModel(BaseModel):
#     __root__: Dict[str, LlmResponseModel]

class LlmCore:
    def __init__(self, text: list, categories: list, prompt: str) -> None:
        self.text = text
        self.categories = categories
        self.prompt = prompt
        # self.client = OpenAiClient()

    async def classify(self) -> dict:
        try:
            logger.info("Calling LLM for classification")
            response = await self.call_llm(self.text, self.categories, self.prompt)
            return response
        except:
            logger.exception("Failed to return categories from LLM")


    async def call_llm(self, text: list, categories: list, prompt: str) -> LlmResponseModel: 
        print(1 + "3")

