import bcrypt
from database.db_manager import DatabaseManager

class AuthService:
    """Handles user registration, login, and security."""
    
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def _hash_password(self, password: str) -> str:
        """Converts a plain text password into a secure hash using native bcrypt."""
        password_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password_bytes, salt)
        return hashed_bytes.decode('utf-8')

    def _verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """Checks if a typed password matches the stored hash."""
        plain_bytes = plain_password.encode('utf-8')
        hashed_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(plain_bytes, hashed_bytes)

    def register_user(self, username: str, password: str, role: str = 'user') -> tuple[bool, str]:
        """Validates input and creates a new user."""
        if len(username) < 3:
            return False, "Username must be at least 3 characters long."
        if len(password) < 6:
            return False, "Password must be at least 6 characters long."
            
        if len(password.encode('utf-8')) > 72:
            return False, "Password is too long. Please use a password under 72 characters."
            
        hashed_pw = self._hash_password(password)
        success = self.db.add_user(username, hashed_pw, role)
        
        if success:
            return True, "Registration successful! You can now log in."
        else:
            return False, "Username already exists. Please choose another."

    def authenticate_user(self, username: str, password: str) -> dict:
        """Verifies credentials and returns user info if successful."""
        user = self.db.get_user_by_username(username)
        
        if user and self._verify_password(password, user['password']):
            return {
                "id": user["id"], 
                "username": user["username"], 
                "role": user["role"]
            }
        return None