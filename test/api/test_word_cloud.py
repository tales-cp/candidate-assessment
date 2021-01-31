import pytest
import http
from fastapi.testclient import TestClient
from project.api.main import app


client = TestClient(app)


class TestWordCloudAPI:
    def test_health_check(self) -> None:
        response = client.get("/word_cloud/bbb21/")
        assert response.status_code == http.HTTPStatus.OK
