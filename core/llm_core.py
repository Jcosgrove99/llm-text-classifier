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

# TODO: How can I make sure this is loosly coupled? ... 
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


    async def _call_llm(self, text: list, categories: list, prompt: str) -> LlmResponseModel: 
        client = OpenAIClient() 

        
        # TODO: look at gemini code in personal website
        
        print(1 + "3")



        # INSERT_YOUR_CODE
        # Prepare the messages for the chat completion
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": "\n".join(text)}
        ]
        # Make the chat completion API call
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.0
        )


