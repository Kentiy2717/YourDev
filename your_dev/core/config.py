from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    LOG_LEVEL: str = 'INFO'
    DEBUG: bool = False

    DATABASE_URL: str = 'postgresql+asyncpg://user:pass@localhost:5432/portfolio'
    SECRET_KEY: str = 'your-secret-key-here'
    ALGORITHM: str = 'HS256'

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7


settings = Settings()