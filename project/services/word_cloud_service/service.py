from typing import Dict, Optional

from project.libs.twitter_client.twitter_client import TwitterClient
from project.services.word_cloud_service.word_cloud import WordCloud


class WordCloudService:
    def __init__(self, twitter_client: TwitterClient) -> None:
        self.client = twitter_client

    def get_word_cloud(self, hashtag: str, max_words: int) -> Optional[WordCloud]:
        word_count: Dict[str, int] = {}
        tweets = self.client.search_by_hashtag(hashtag)

        for tweet in tweets:
            self._update_word_count(tweet.text, word_count)

        ordered_count = self._remove_exceeding_words(word_count, max_words)

        return WordCloud(
            word_count=ordered_count,
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

    def _remove_exceeding_words(
        self, word_count: Dict[str, int], max_words: int
    ) -> Dict[str, int]:
        ordered_dict = {
            k: v
            for k, v in sorted(
                word_count.items(), key=lambda item: item[1], reverse=True
            )[:max_words]
        }

        return ordered_dict
