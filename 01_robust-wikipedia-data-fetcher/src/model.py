# This file:

# Defines what “valid data” looks like
# Protects your pipeline from bad API responses
# Makes your system predictable and reliable

# It is like blueprint of our data structure
from pydantic import BaseModel,Field,HttpUrl
from typing import List, Optional

class WikiArticle(BaseModel):
    """
    Data model representing a validated Wikipedia article.
    This ensures all external API data is structured and reliable.
    """
    title: str = Field(..., description="The title of the Wikipedia article")
    url:HttpUrl =Field(..., description="The URL of the Wikipedia article")
    summary: str = Field(..., description="A brief summary of the Wikipedia article")
    categories: List[str] = Field(None, description="List of categories the article belongs to")
    last_edited: Optional[str] = Field(None, description="Timestamp of the last edit to the article")

# if we want to forbid extra fields not defined in the model
    class Config:
        extra = "forbid"
