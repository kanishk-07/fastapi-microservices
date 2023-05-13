from pydantic import BaseSettings

class Settings(BaseSettings):
    PAYMENT_DB_URL: str
    PAYMENT_DB_PORT: int
    PAYMENT_DB_PASSWORD: str

    class Config:
        env_file = ".env"
        

settings = Settings()