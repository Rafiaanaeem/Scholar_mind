# create_admin.py

from config.settings import settings
from database.db_manager import DatabaseManager
from services.auth_service import AuthService

def create_master_admin():
    print("🛡️ ScholarMind Pro - Admin Creation Utility")
    print("-" * 40)
    
    # 1. Connect to the database and authentication service
    db = DatabaseManager(settings.DB_PATH)
    auth = AuthService(db)
    
    # 2. Ask you (the developer) for the admin credentials
    username = input("Enter your desired Admin Username: ")
    password = input("Enter your desired Admin Password: ")
    
    # 3. Use the auth service to register the user, but FORCE the role to 'admin'
    success, message = auth.register_user(username, password, role="admin")
    
    if success:
        print(f"\n✅ SUCCESS! Admin account '{username}' has been created.")
        print("You can now log in through the web app and access the Admin Dashboard.")
    else:
        print(f"\n❌ ERROR: {message}")

if __name__ == "__main__":
    create_master_admin()