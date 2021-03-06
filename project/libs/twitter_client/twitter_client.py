from typing import List

import tweepy

from project.libs.twitter_client.tweet import Tweet
from project.libs.twitter_client.twitter_client_config import TwitterClientConfig
from datetime import datetime
from datetime import timedelta


class TwitterClient:
    def __init__(self, config: TwitterClientConfig):
        twitter_auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        twitter_auth.set_access_token(config.access_token, config.access_token_secret)

        self.api = tweepy.API(twitter_auth)

    def search_by_hashtag(self, hashtag: str, max_items: int = 100) -> List[Tweet]:
        tweets: List[Tweet] = []
        for tweet in tweepy.Cursor(
            self.api.search_30_day,
            environment_name="dev",
            query=f"#{hashtag}",
            fromDate=(datetime.today() - timedelta(days=1)).strftime("%Y%m%d%H%M"),
        ).items(max_items):
            tweets.append(
                Tweet(
                    text=tweet.text,
                    timestamp=tweet.created_at.strftime("%m/%d/%Y, %H:%M:%S"),
                )
            )
        return tweets
