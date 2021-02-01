from typing import Union

from fastapi import HTTPException, Response
from fastapi.routing import APIRouter
from project.config import settings
from project.services.word_cloud_service.word_cloud import WordCloud
from project.libs.twitter_client.twitter_client import TwitterClient
from project.libs.twitter_client.twitter_client_config import TwitterClientConfig
from project.services.word_cloud_service.service import WordCloudService


router = APIRouter()

twitter_client = TwitterClient(
    TwitterClientConfig(
        consumer_key=settings.CONSUMER_KEY,
        consumer_secret=settings.CONSUMER_SECRET,
        access_token=settings.ACCESS_TOKEN,
        access_token_secret=settings.ACCESS_TOKEN_SECRET,
    )
)

word_cloud_service = WordCloudService(twitter_client)


@router.get("/word_cloud/{hashtag}/")
def get_word_cloud(
    hashtag: str, max_words: int = 100, response_format: str = "json"
) -> Union[WordCloud, Response]:
    word_cloud_response = word_cloud_service.get_word_cloud(hashtag, max_words)
    if not word_cloud_response:
        raise HTTPException(status_code=404, detail="Hashtag not found")

    if response_format == "csv":
        return Response(content=word_cloud_response.to_csv(), media_type="text/csv")

    return word_cloud_response
