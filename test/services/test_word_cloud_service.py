from typing import List, cast

import pytest
from datetime import datetime

from project.libs.twitter_client.tweet import Tweet
from project.libs.twitter_client.twitter_client import TwitterClient
from project.services.word_cloud_service.service import WordCloudService


class MockedTwitterClient:
    def search_by_hashtag(self, hashtag: str, max_items: int = 100) -> List[Tweet]:
        return [
            Tweet(
                text="I am the grandson of the father of my father #something",
                timestamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            ),
            Tweet(
                text="RT Luke, I am your father #something",
                timestamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            ),
        ]


class TestWordCloudService:
    @pytest.fixture()
    def twitter_client(self) -> TwitterClient:
        client = MockedTwitterClient()
        return cast(TwitterClient, client)

    @pytest.fixture()
    def word_cloud_service(self, twitter_client: TwitterClient) -> WordCloudService:
        return WordCloudService(twitter_client)

    def test_update_word_count(self, word_cloud_service: WordCloudService) -> None:
        word_cloud = word_cloud_service.get_word_cloud("something", 100)
        assert word_cloud.word_count["father"] == 3  # type: ignore
        assert word_cloud.word_count.get("rt") is None  # type: ignore
