import streamlit as st

def load_custom_css():
    """Injects custom CSS to enhance the application UI."""
    st.markdown("""
        <style>
        .main-header {
            font-size: 2.2rem;
            font-weight: 700;
            color: #1E3A8A;
            margin-bottom: 0.5rem;
        }
        .sub-header {
            font-size: 1.1rem;
            color: #4B5563;
            margin-bottom: 2rem;
        }
        .stButton>button {
            border-radius: 8px;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

def render_header():
    """Renders the standard ScholarMind Pro top banner."""
    load_custom_css()
    st.markdown('<div class="main-header">🎓 ScholarMind Pro</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">AI-Powered Academic Research Assistant</div>', unsafe_allow_html=True)
    st.divider()

def render_sidebar():
    """Renders the left sidebar navigation and user status."""
    st.sidebar.title("📌 Navigation")
    
    if st.session_state.get('authenticated', False):
        user = st.session_state.get('user', {})
        st.sidebar.success(f"Logged in as: **{user.get('username', 'User')}**")
        st.sidebar.caption(f"Role: {user.get('role', 'user').capitalize()}")
        
        pages = ["Research Workspace", "Research History"]
        if user.get('role') == 'admin':
            pages.append("Admin Dashboard")
            
        selected_page = st.sidebar.radio("Go to:", pages)
        
        st.sidebar.divider()
        if st.sidebar.button("🚪 Logout", use_container_width=True):
            logout_user()
            
        return selected_page
    return "Auth"

def logout_user():
    """
    CRITICAL SECURITY FIX:
    Wipes all session variables to prevent memory leakage between user logins.
    """
    keys_to_clear = [
        'authenticated', 'user', 'current_topic', 
        'generated_content', 'topic_suggestions'
    ]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]
    
    st.rerun()