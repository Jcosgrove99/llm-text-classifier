from dotenv import load_dotenv
load_dotenv()
import os
import json
from google import genai
from pydantic import BaseModel
from prompt_builder import PromptBuilder
import pprint

class Response(BaseModel):
    answer: bool

class ResponseCategory(BaseModel): 
    category: str
    log_prob: float

class ClassifyOutput(BaseModel): 
    input_text: str
    response: ResponseCategory

# Gemini API Docs
# https://ai.google.dev/gemini-api/docs
GEMINI_2_0_FLASH = "gemini-2.0-flash" #Gemini 2.0 Flash delivers next-gen features and improved capabilities
GEMINI_2_5_FLASH_05_20 = "gemini-2.5-flash-preview-05-20" #Our best model in terms of price-performance, offering well-rounded capabilities
GEMINI_2_5_PRO_06_05 = "gemini-2.5-pro-preview-06-05" #Gemini 2.5 Pro is our state-of-the-art thinking model


api_key = os.getenv('GEMINI_API_KEY', None)
if api_key is None:
    raise ValueError("GEMINI_API_KEY is not set")


# LLM class
class Gemini:
    def __init__(self, model: str) -> None:
        self.model = model
        self.prompt_builder = PromptBuilder()
        self.client = genai.Client(api_key=api_key)

    def ask(self, prompt:str, model:str): #TODO: Specify the response type here
        response = self.client.models.generate_content(
            model=model, contents=prompt
        )
        return response
    
    def ask_bool(self, prompt:str, model:str) -> bool: 
        prompt = prompt + "/n Provide your answer as True or False."
        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": [ClassifyOutput],
            },
        )

        response_json = json.loads(response.text)
        return response_json.get("answer")
    
    def classify(self, prompt:str, categories: list[str], input_text:list[str]) -> list[ResponseCategory]:
        user_prompt = self.prompt_builder.build_user_prompt(prompt, categories, input_text)
        print(user_prompt)
        response = self.client.models.generate_content(
            model=self.model,
            contents=user_prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": ClassifyOutput,
            },
        )
        print(response.text)


llm = Gemini(GEMINI_2_0_FLASH)
llm.classify("You are an expert economist. Place these in the following categories", 
             ["good", "bad", "nuetral"], 
             ["whats wrong with you?!", "the food was great"]
             )
# response = llm.ask("is it working?", GEMINI_2_0_FLASH)
# response = llm.ask_bool("Is it true that the sky is blue?", GEMINI_2_0_FLASH)
#llm.classify("Tell me if this is good or bad", GEMINI_2_0_FLASH, "this food was awful")

