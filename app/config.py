from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str
    database_url: str
    secret: str

    class Config:
        env_file = '.env'
        extra = 'ignore'


settings = Settings()
