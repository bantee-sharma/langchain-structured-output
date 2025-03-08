from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, Optional
from dotenv import load_dotenv
import warnings

warnings.filterwarnings("ignore", message="can not use method 'json_schema'")

load_dotenv()

# Initialize Model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Corrected Schema
class ReviewSchema(TypedDict):
    keys: list[str]  # List of key points
    summary: str  # A brief summary of the review
    sentiment: str  # Either "Positive" or "Negative"
    pros: Optional[list[str]]  # List of pros (optional)
    cons: Optional[list[str]]  # List of cons (optional)
    name: Optional[str]  # Reviewer's name (optional)

# Define structured output with descriptions
struc_model = model.with_structured_output(
    schema=ReviewSchema,  # Pass the corrected schema
    description="Extract key points, summary, sentiment, pros, and cons from a product review."
)

# Test Input
res = struc_model.invoke(
    """Upgraded to the 16 from my 12 and it is a great phone. The Ultramarine Blue looks and feels sooo good. 
    The photos don't do enough justice to this variant.

    You definitely do not need to upgrade to this if you are having a 14 or a 15, unless Apple Intelligence 
    is something that you do not want to live without.
    
    Camera is great, though not very sure of the Camera Control thing, cuz all that is pretty much available on-screen UI.

    Also, got a great deal on the exchange and bank offer, so zero complaints."""
)

print(res)
