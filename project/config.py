from dynaconf import Dynaconf, Validator


settings = Dynaconf(
    envvar_prefix=False,
    environments=True,
    validators=[
        Validator(
            "DB_CONNECTION_STRING",
            must_exist=True,
        ),
        Validator("HOSTNAME", is_type_of=str, default=""),
        Validator("PORT", is_type_of=int, default=5000),
        Validator("HOST", is_type_of=str, default="0.0.0.0"),
    ],
)
