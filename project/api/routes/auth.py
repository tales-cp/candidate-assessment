from fastapi import HTTPException

from fastapi import Security
from fastapi.routing import APIRouter
from fastapi.security import APIKeyQuery, APIKeyHeader
from starlette.status import HTTP_403_FORBIDDEN

API_KEY = "abcdefghijklmnopqrstuvxz"
API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)


router = APIRouter()


async def get_api_key(
    key_query: str = Security(api_key_query),
    key_header: str = Security(api_key_header),
) -> str:
    if key_query == API_KEY:
        return key_query
    elif key_header == API_KEY:
        return key_header
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
        )
