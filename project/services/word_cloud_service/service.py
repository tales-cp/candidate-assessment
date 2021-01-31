from typing import Dict, Optional

from project.libs.twitter_client.twitter_client import TwitterClient
from project.services.word_cloud_service.word_cloud import WordCloud


class WordCloudService:
    def __init__(self, twitter_client: TwitterClient) -> None:
        self.client = twitter_client

    def get_word_cloud(self, hashtag: str, max_items: int) -> Optional[WordCloud]:
        word_count: Dict[str, int] = {}
        tweets = self.client.search_by_hashtag(hashtag, max_items)

        for tweet in tweets:
            self._update_word_count(tweet.text, word_count)

        return WordCloud(
            word_count=word_count,
            topic=hashtag,
            first_tweet_date=tweets[0].timestamp,
            last_tweet_date=tweets[-1].timestamp,
        )

    def _update_word_count(self, text: str, word_count: Dict[str, int]) -> None:
        for word in text.split():
            normalized_word = word.lower()
            if normalized_word.startswith("#") or normalized_word == "rt":
                continue
            if word_count.get(normalized_word):
                word_count[normalized_word] += 1
            else:
                word_count[normalized_word] = 1
