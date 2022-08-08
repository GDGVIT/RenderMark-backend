from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL = "sqlite:///./app_db.db"
    API_V1_STR: str = "/api/v1"


settings = Settings()
