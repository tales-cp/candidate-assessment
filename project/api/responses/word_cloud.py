from typing import Dict

from pydantic import BaseModel


class WordCloudResponse(BaseModel):
    word_count: Dict[str, int]
    topic: str
    first_tweet_date: str
    last_tweet_date: str
