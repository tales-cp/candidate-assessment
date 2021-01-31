from pydantic import BaseModel


class TwitterClientConfig(BaseModel):
    consumer_key: str
    consumer_secret: str
    access_token: str
    access_token_secret: str
