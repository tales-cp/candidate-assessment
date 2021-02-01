import http
from fastapi.testclient import TestClient
from project.api.main import app


client = TestClient(app)


class TestMainAPI:
    def test_health_check(self) -> None:
        response = client.get("/")
        assert response.status_code == http.HTTPStatus.OK
