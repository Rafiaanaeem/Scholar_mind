import logging
import os

if not os.path.exists('logs'):
    os.makedirs('logs')

def setup_logger():
    """Configures and returns a standard logger for the application."""
    
    logger = logging.getLogger("ScholarMind")
    
    if not logger.handlers:
        logger.setLevel(logging.DEBUG) 
        
        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO) 
        
        f_handler = logging.FileHandler('logs/app.log')
        f_handler.setLevel(logging.ERROR) 
    
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(formatter)
        f_handler.setFormatter(formatter)
        
        logger.addHandler(c_handler)
        logger.addHandler(f_handler)
        
    return logger

logger = setup_logger()