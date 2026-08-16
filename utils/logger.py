import logging
import os

# Create a logs directory if it doesn't exist
if not os.path.exists('logs'):
    os.makedirs('logs')

def setup_logger():
    """Configures and returns a standard logger for the application."""
    
    # Create a custom logger
    logger = logging.getLogger("ScholarMind")
    
    # Prevent adding multiple handlers if the logger already exists
    if not logger.handlers:
        logger.setLevel(logging.DEBUG) # Catch everything from DEBUG and above
        
        # Create handlers
        # 1. Console Handler (Shows in your VS Code terminal)
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO) # Only show INFO, WARNING, ERROR in terminal
        
        # 2. File Handler (Saves secretly to a file for debugging later)
        f_handler = logging.FileHandler('logs/app.log')
        f_handler.setLevel(logging.ERROR) # Only save actual ERRORS to the file
        
        # Create formatting (How the message looks)
        # Example: 2026-08-16 14:30:00 - ScholarMind - ERROR - Database failed
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(formatter)
        f_handler.setFormatter(formatter)
        
        # Add handlers to the logger
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        
    return logger

# Create a single instance to be used across the app
logger = setup_logger()