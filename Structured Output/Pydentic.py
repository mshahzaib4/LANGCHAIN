from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from pydantic import BaseModel, Field

load_dotenv()
model = ChatOpenAI()
# Write The review of software house in 100 words in setence

review = "Write a review of a software house in 100 words in sentence format. The review should be positive, highlighting the strengths of the software house, such as their expertise, quality of work, and customer service. It should also mention any specific projects or technologies they excel in. The tone should be professional and appreciative, suitable for a business context. Name the author of the review as 'M Shahzaib Yaqoob'."

class ReviewRequest(BaseModel):
    sentiment: list[str] = Field(description="The sentiment of the review, e.g., positive, negative, neutral")
    length: int = Field(description="The desired length of the review in words")
    name_author: str = Field(description="The name of the author of the review")

structural_model = model.with_structured_output(ReviewRequest, method='function_calling')
result = structural_model.invoke(review)
print(result)


