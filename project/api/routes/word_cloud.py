import tweepy
from fastapi.routing import APIRouter
from project.config import settings
from project.api.responses.word_cloud import WordCloudResponse


router = APIRouter()


twitter_auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
twitter_auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

twitter_client = tweepy.API(twitter_auth)


@router.get("/word_cloud/{hashtag}")
def get_word_cloud(hashtag: str) -> WordCloudResponse:
    return WordCloudResponse(
        word_count={},
        topic="",
        first_tweet_date="10/10/2021",
        last_tweet_date="10/10/2021",
    )
