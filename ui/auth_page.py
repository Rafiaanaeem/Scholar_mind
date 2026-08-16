import streamlit as st
from services.auth_service import AuthService
from ui.components import render_header

def render_auth_page(auth_service: AuthService):
    """Renders the login and registration UI."""
    render_header()
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])
        
        with tab1:
            st.subheader("Welcome Back")
            login_username = st.text_input("Username", key="login_user")
            login_password = st.text_input("Password", type="password", key="login_pass")
            
            if st.button("Sign In", use_container_width=True, type="primary"):
                if login_username and login_password:
                    user_data = auth_service.authenticate_user(login_username, login_password)
                    if user_data:
                        st.session_state['authenticated'] = True
                        st.session_state['user'] = user_data
                        st.success(f"Welcome back, {user_data['username']}!")
                        st.rerun()
                    else:
                        st.error("Invalid username or password.")
                else:
                    st.warning("Please fill in all fields.")
                    
        with tab2:
            st.subheader("Create an Account")
            reg_username = st.text_input("Username", key="reg_user")
            reg_password = st.text_input("Password", type="password", key="reg_pass")
            reg_confirm = st.text_input("Confirm Password", type="password", key="reg_confirm_pass")
            
            if st.button("Register Account", use_container_width=True):
                if reg_username and reg_password and reg_confirm:
                    if reg_password != reg_confirm:
                        st.error("Passwords do not match!")
                    else:
                        success, message = auth_service.register_user(reg_username, reg_password)
                        if success:
                            st.success(message)
                        else:
                            st.error(message)
                else:
                    st.warning("Please fill in all fields.")