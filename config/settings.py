import os
from dotenv import load_dotenv

# Load the variables from the .env file into the system environment
load_dotenv()

class Config:
    """Central configuration for ScholarMind Pro."""
    
    # AI Settings
    # GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    # GEMINI_MODEL = "gemini-1.5-flash" 
    GROQ_API_KEY=os.getenv("GROQ_API_KEY")
    GROQ_MODEL=os.getenv("GROQ_MODEL")
    
    # Database Settings
    DB_PATH = "scholarmind.db"
    
    # Application Settings
    APP_NAME = "ScholarMind Pro"
    APP_VERSION = "2.0.0"

# Create a single instance to be imported by other files
settings = Config()

