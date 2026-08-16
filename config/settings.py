import os
from dotenv import load_dotenv

load_dotenv()  # to load the environment variables

class Config:
    """Central configuration for ScholarMind Pro."""
    
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    GROQ_MODEL=os.getenv("GROQ_MODEL")
    
    DB_PATH = "scholarmind.db"
    
    APP_NAME = "ScholarMind "
    APP_VERSION = "2.0.0"

settings = Config()  # instance created

