from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str
    app_name: str

    database_host: str
    database_port: int = 5432
    database_name: str
    database_user: str
    database_pass: str

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.database_user}:{self.database_pass}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )

    class Config:
        env_file = ".env"


settings = Settings()