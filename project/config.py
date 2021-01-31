from dynaconf import Dynaconf, Validator


settings = Dynaconf(
    envvar_prefix=False,
    environments=True,
    load_dotenv=True,
    validators=[
        Validator(
            "DB_CONNECTION_STRING",
            "CONSUMER_KEY",
            "CONSUMER_SECRET",
            "ACCESS_TOKEN",
            "ACCESS_TOKEN_SECRET",
            must_exist=True,
        ),
        Validator("HOSTNAME", is_type_of=str, default=""),
        Validator("PORT", is_type_of=int, default=5000),
        Validator("HOST", is_type_of=str, default="0.0.0.0"),
    ],
)
