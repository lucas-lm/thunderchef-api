from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
   
  model_config = SettingsConfigDict(env_file='.env')

  openai_api_key: str
  openai_admin_key: str