import http
from fastapi.testclient import TestClient
from project.api.main import app


client = TestClient(app)


class TestWordCloudAPI:
    def test_word_cloud(self) -> None:
        response = client.get("/word_cloud/bbb21/?access_token=1234567asdfgh")
        assert response.status_code == http.HTTPStatus.OK

    def test_word_cloud_without_access_key(self) -> None:
        response = client.get("/word_cloud/bbb21/")
        assert response.status_code == http.HTTPStatus.FORBIDDEN
