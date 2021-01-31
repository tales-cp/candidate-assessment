import uvicorn
from project.config import settings

from fastapi import FastAPI

app = FastAPI()


@app.get("/health_check/")
def health_check() -> str:
    return "OK"


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.PORT,
        debug=settings.DEBUG,
        access_log=False,
    )
