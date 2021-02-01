import uvicorn
from project.config import settings
from project.api.routes import word_cloud
from fastapi import FastAPI

app = FastAPI()

app.include_router(word_cloud.router, tags=["word cloud"])


@app.get("/")
def health_check() -> str:
    return ""


if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=settings.PORT,
        debug=settings.DEBUG,
        access_log=False,
    )
