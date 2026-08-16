import streamlit as st

from config.settings import settings
from database.db_manager import DatabaseManager
from services.auth_service import AuthService
from services.ai_service import AIService
from ui.components import render_sidebar
from ui.auth_page import render_auth_page
from ui.research_page import render_research_page
from ui.admin_page import render_admin_page

st.set_page_config(
    page_title=settings.APP_NAME,
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)
@st.cache_resource
def init_services():
    db = DatabaseManager(settings.DB_PATH)
    auth = AuthService(db)
    ai = AIService()
    return db, auth, ai

db_manager, auth_service, ai_service = init_services()

def main():
    """Main routing function for the application."""
    
    selected_page = render_sidebar()
    
    if not st.session_state.get('authenticated', False):
        render_auth_page(auth_service)
    else:
        if selected_page in ["Research Workspace", "Research History"]:
            render_research_page(ai_service, db_manager, selected_page)
        elif selected_page == "Admin Dashboard":
            render_admin_page(db_manager)

if __name__ == "__main__":
    main()