from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from core.security import create_access_token

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        header = request.headers.get("Authorization")
        if not header:
            return Response("Missing token", status_code=401)

        token = header.split(" ")[1]
        if token != create_access_token({"sub": "username"}):  # This is just a sample. You should decode the token and check if it's valid.
            return Response("Invalid token", status_code=401)

        response = await call_next(request)
        return response
