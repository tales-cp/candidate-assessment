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
def get_word_cloud(hashtag: str) -> WordCloud:
    tweets = word_cloud_service.get_word_cloud(hashtag, 100)

    return WordCloud(
        word_count={},
        topic="",
        first_tweet_date="10/10/2021",
        last_tweet_date="10/10/2021",
    )
