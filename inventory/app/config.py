from pydantic import BaseSettings

class Settings(BaseSettings):
    REDIS_DB_URL: str
    REDIS_DB_PORT: int
    REDIS_DB_PASSWORD: str

    class Config:
        env_file = ".env"
        

settings = Settings()