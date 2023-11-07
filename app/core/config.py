from starlette.config import Config
from pydantic_settings import BaseSettings

config = Config(".env")

class Settings(BaseSettings):
    database_url: str = config("DATABASE_URL", cast=str)
    secret_key: str = config("SECRET_KEY", cast=str)
    access_token_expire_minutes: int = config("ACCESS_TOKEN_EXPIRE_MINUTES", cast=int, default=30)

settings = Settings()
