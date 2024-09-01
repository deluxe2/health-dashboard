from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings, frozen=True):
    # Database
    db_url: str
    db_name: str
    # Auth
    server_metadata_url: str
    client_id: str
    client_secret: str
    group_scope: str
    admin_group: str
    # Session
    session_secret: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
