from typing import Dict

from pydantic import BaseModel


class WordCloud(BaseModel):
    word_count: Dict[str, int]
    topic: str
    first_tweet_date: str
    last_tweet_date: str

    def to_csv(self) -> str:
        csv_content = ""
        csv_content += "word, count, topic, first_tweet_date, last_tweet_date\n"
        for count in self.word_count.items():
            csv_content += (
                f"{count[0]}, {count[1]}, {self.topic}, {self.first_tweet_date}, "
                f"{self.last_tweet_date}\n"
            )

        return csv_content
