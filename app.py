import streamlit as st

# 1. Import our configurations and services
from config.settings import settings
from database.db_manager import DatabaseManager
from services.auth_service import AuthService
from services.ai_service import AIService

# 2. Import our UI pages
from ui.components import render_sidebar
from ui.auth_page import render_auth_page
from ui.research_page import render_research_page
from ui.admin_page import render_admin_page

# 3. Configure the Streamlit Page (Must be the first Streamlit command)
st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 4. Initialize Services (Dependency Injection)
# We use st.cache_resource so we only connect to the database once, not every time the user clicks a button!
@st.cache_resource
def init_services():
    db = DatabaseManager(settings.DB_PATH)
    auth = AuthService(db)
    ai = AIService()
    return db, auth, ai

db_manager, auth_service, ai_service = init_services()

def main():
    """Main routing function for the application."""
    
    # Render the sidebar and get the user's requested page
    selected_page = render_sidebar()
    
    # Route the user based on authentication status
    if not st.session_state.get('authenticated', False):
        # User is not logged in, show the login/register page
        render_auth_page(auth_service)
    else:
        # User is logged in, route to the correct workspace
        if selected_page in ["Research Workspace", "Research History"]:
            render_research_page(ai_service, db_manager, selected_page)
        elif selected_page == "Admin Dashboard":
            render_admin_page(db_manager)

if __name__ == "__main__":
    main()