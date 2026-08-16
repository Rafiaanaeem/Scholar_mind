import streamlit as st
import pandas as pd
from database.db_manager import DatabaseManager
from ui.components import render_header

def render_admin_page(db_manager: DatabaseManager):
    """Renders the admin dashboard to manage users."""
    render_header()
    
    # 🔒 Authorization Check: Double-check that the user is actually an admin
    user = st.session_state.get('user', {})
    if user.get('role') != 'admin':
        st.error("Unauthorized Access. You do not have permission to view this page.")
        return
        
    st.subheader("🛡️ Admin Dashboard")
    st.write("Welcome to the administration panel. Here you can view all registered users.")
    
    # Fetch all users from the database manager
    users = db_manager.get_all_users()
    
    if not users:
        st.info("No users found in the database.")
        return
        
    # Convert the raw database data into a clean Pandas DataFrame for Streamlit to display
    df = pd.DataFrame(users, columns=['ID', 'Username', 'Role', 'Date Joined'])
    
    # Display as a clean, interactive table
    st.dataframe(
        df, 
        use_container_width=True, 
        hide_index=True
    )