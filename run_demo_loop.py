from core.llm_core import LlmCore
import pandas as pd

# TEST DATA ---------------------------------
data = pd.read_csv("data/combined_tweets.csv")
text_array = data["text"]
categories = ["good", "bad", "nuetral"]
prompt = "please place these comma seperated values into one of the following categories."
# --------------------------------------------

llm_core = LlmCore(text=text_array, categories=categories, prompt=prompt)

import asyncio

async def demo_loop():
    response = await llm_core.classify()

if __name__ == "__main__":
    asyncio.run(demo_loop())

#category_output_json = llm_core.output() 

# Example category_output_json 
# TODO: but what if the input text is identical?...
# that wouldn't be a problem. 
{
    "input text ....": {
        "llmCategory": "negative",


        "llmLogProb": 0.92
    },
    "input text ....": {
        "llmCategory": "negative",
        "llmLogProb": 0.92
    }
}
