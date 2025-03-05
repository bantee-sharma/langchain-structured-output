from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

# schema

class review(TypedDict):
    summary: str
    sentiment: str


struc_model = model.with_structured_output(review)

res = struc_model.invoke("""Upgraded to the 16 from my 12 and it is a great phone. The Ultramarine Blue looks and feels sooo good. The photos don't do enough justice to this variant.

You definitely do not need to upgrade to this if you are having a 14 or a 15, unless Apple Intelligence is something that you do not want to live without.
Camera is great, though not very sure of the Camera Control thing, cuz all that is pretty much available on-screen UI.

Also, got a great deal on the exchange and bank offer, so zero complaints.""")

print(res)
