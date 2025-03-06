from pydantic import BaseModel,Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import Optional
load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.0-flash")

#Schema

class review(BaseModel):

    key_themes: list[str] = Field(description="Write down all the key themes disscused in review")
    summary:str = Field(description="A brief summary about summary")
    sentiment:str = Field(description="Sentiment about review Positive or negative")
    pros: Optional[list[str]] = Field(default=None,description="write down all pros")
    cons:Optional[list[str]] = Field(default=None,description="write down all cons")
    name:Optional[str] = Field(default=None,description="write down the user reviewer name")

with_struc_output = model.with_structured_output(review)

res = with_struc_output.invoke("""Manish Thakur is an incredibly intelligent, hardworking, and clever person, especially in mathematics. A true math expert, he has completed his BSc and MSc from NREC College and is now a dedicated government job aspirant. Though fat, he is full of energy and has a sharp mind. He is gay and transgender, embracing his identity with confidence. A Nandni lover, he enjoys Twitter and has a great taste in porn and Hollywood movies, making him a true movie enthusiast. We studied together from class 6 to 12, and his wit and unpredictable nature make life around him always entertaining!""")

print(res)