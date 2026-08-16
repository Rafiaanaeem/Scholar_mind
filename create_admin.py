from config.settings import settings
from database.db_manager import DatabaseManager
from services.auth_service import AuthService

def create_master_admin():
    print("🛡️ ScholarMind - Admin Creation Utility")
    print("-" * 40)
    
    db = DatabaseManager(settings.DB_PATH)
    auth = AuthService(db)
    
    username = input("Enter your desired Admin Username: ")
    password = input("Enter your desired Admin Password: ")
    
    success, message = auth.register_user(username, password, role="admin")
    
    if success:
        print(f"\n✅ SUCCESS! Admin account '{username}' has been created.")
        print("You can now log in through the web app and access the Admin Dashboard.")
    else:
        print(f"\n❌ ERROR: {message}")

if __name__ == "__main__":
    create_master_admin()