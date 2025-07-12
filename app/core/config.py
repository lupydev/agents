from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    API: str = "agents/"
    PROJECT_NAME: str = "AI Agents"

    # postgres
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_URL: str

    # OPENAI
    OPENAI_API_KEY: str

    # PINECONE
    PINECONE_API_KEY: str

    # SEARCHAPI
    SERAPI_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
