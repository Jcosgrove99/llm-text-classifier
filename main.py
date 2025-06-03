# FastAPI 
# Input: Prompt, 1-D Array, Categories
# Output: 2 Arrays, 1. Categories, 2. LogProbs 

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Any
from core.llm_core import LlmCore

app = FastAPI(
    title="llm-text-classifier",
    version="1.0.0"
)

llm_core = LlmCore() 

class ClassifyRequest(BaseModel):
    prompt: str
    array: List[str]
    categories: List[str]

class ClassifyResponse(BaseModel):
    categories: List[str]
    logprobs: List[float]

@app.get("/health")
def health():
    return {"status": "it's healthy dude"}

@app.post("/classify", response_model=ClassifyResponse)
def classify(request: ClassifyRequest):
    # Dummy implementation: assign random logprobs for demonstration
    # In a real implementation, you would call your LLM here
    if not request.categories:
        raise HTTPException(status_code=400, detail="Categories list cannot be empty.")
    
    # TODO: Implement llm classification method 
    # response = await llm_core.get_llm_classification()
    import random
    logprobs = [random.uniform(-2.0, 0.0) for _ in request.categories]
    return ClassifyResponse(categories=request.categories, logprobs=logprobs)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
