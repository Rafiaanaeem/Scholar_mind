import sqlite3
import os

class DatabaseManager:
    """Handles all database interactions for ScholarMind Pro."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._initialize_db()

    def get_connection(self):
        """Creates and returns a connection to the SQLite database."""
        return sqlite3.connect(self.db_path, check_same_thread=False)

    def _initialize_db(self):
        """Creates the necessary tables if they do not exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Users Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    role TEXT DEFAULT 'user',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Research History Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS research_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    topic TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            conn.commit()

    def add_user(self, username: str, hashed_password: str, role: str = 'user') -> bool:
        """Adds a new user. Returns True if successful, False if username exists."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO users (username, password, role) VALUES (?, ?, ?)", 
                    (username, hashed_password, role)
                )
                conn.commit()
                return True
        except sqlite3.IntegrityError:
            return False

    def get_user_by_username(self, username: str) -> dict:
        """Retrieves user data by username."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, password, role FROM users WHERE username = ?", (username,))
            row = cursor.fetchone()
            if row:
                return {"id": row[0], "username": row[1], "password": row[2], "role": row[3]}
            return None

    def get_all_users(self) -> list:
        """Retrieves all users for the Admin Dashboard."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, role, created_at FROM users")
            return cursor.fetchall()

    def save_research(self, user_id: int, topic: str, content: str) -> bool:
        """Saves generated AI research."""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO research_history (user_id, topic, content) VALUES (?, ?, ?)",
                    (user_id, topic, content)
                )
                conn.commit()
                return True
        except Exception as e:
            print(f"Database Error: {e}")
            return False

    def get_user_history(self, user_id: int) -> list:
        """Retrieves research history for a specific user."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, topic, content, created_at FROM research_history WHERE user_id = ? ORDER BY created_at DESC", 
                (user_id,)
            )
            return cursor.fetchall()