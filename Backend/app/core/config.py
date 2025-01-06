from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MyFastAPI App"
    DEBUG: bool = True
    API_V1_STR: str = "/api/v1"
    
    # Database configuration
    DATABASE_URL: str = "sqlite:///./test.db"
    
    class Config:
        case_sensitive = True

settings = Settings() 