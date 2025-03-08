from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict,Annotated,Optional
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore", message="can not use method 'json_schema'")

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

# Schema

class Review(TypedDict):
    
    keys: Annotated[list[str],"write down all the key"]
    summary: Annotated[str,"A brief summary of review"]
    sentiment: Annotated[str,"return sentiment of review either Negative or Positive"]
    pros: Annotated[Optional[list[str]],"write down all pros"]
    cons: Annotated[Optional[list[str]],"write down all cons"]
    name: Annotated[Optional[str],"name of the reviewer"]

struc_model = model.with_structured_output(Review)


res = struc_model.invoke("""Upgraded to the 16 from my 12 and it is a great phone. The Ultramarine Blue looks and feels sooo good. The photos don't do enough justice to this variant.

You definitely do not need to upgrade to this if you are having a 14 or a 15, unless Apple Intelligence is something that you do not want to live without.
Camera is great, though not very sure of the Camera Control thing, cuz all that is pretty much available on-screen UI.

Also, got a great deal on the exchange and bank offer, so zero complaints.""")

print(res)
