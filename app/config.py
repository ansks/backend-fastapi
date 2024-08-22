from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ValidationError

class Settings(BaseSettings):
    """It checks in the environment file and from environment. 
    if variable not found then it will throw error. """
    
    # database_name: str = "localhost"
    # database_password: str = "267766ks"
    # secret_key: str = "14w5"
    
    # model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
    
    database_hostname: str
    database_port: int
    database_username: str
    database_password: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int
    
    class Config:
        env_file = ".env"
    

settings = Settings()
