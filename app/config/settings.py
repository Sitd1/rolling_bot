from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field

# Загружаем переменные окружения из .env файла
load_dotenv()

# Base
class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra="ignore")


# TeleGram
class TelegramConfig(ConfigBase):
    model_config = SettingsConfigDict(env_prefix="TELEGRAM_")
    bot_token: SecretStr


# DataBase
class DatabaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="db_")

    user: str
    password: SecretStr
    name: str
    host: str
    port: int


    @property
    def url_asyncpg(self) -> str:
        """PostgreSQL URL для asyncpg"""
        return f"postgresql+asyncpg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}"

    @property
    def url_psycopg(self) -> str:
        """PostgreSQL URL для psycopg"""
        return f"postgresql+psycopg://{self.user}:{self.password.get_secret_value()}@{self.host}:{self.port}/{self.name}"


class Config(BaseSettings):
    tg: TelegramConfig = Field(default_factory=TelegramConfig)


config = Config()

if __name__ == "__main__":
    print(config.tg.bot_token)
