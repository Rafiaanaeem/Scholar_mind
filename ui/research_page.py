import streamlit as st
from services.ai_service import AIService
from services.export_service import ExportService
from database.db_manager import DatabaseManager
from ui.components import render_header
from utils.time_utils import utc_to_local

def render_research_page(ai_service: AIService, db_manager: DatabaseManager, active_tab: str):
    """Renders either the main generation page or history based on sidebar selection."""
    render_header()
    user = st.session_state.get('user', {})
    
    if active_tab == "Research Workspace":
        _render_workspace(ai_service, db_manager, user)
    elif active_tab == "Research History":
        _render_history(db_manager, user)

def _render_workspace(ai_service: AIService, db_manager: DatabaseManager, user: dict):
    """Workspace section for topic discovery and research generation."""
    
    st.subheader("💡 Phase 1: Topic Discovery")
    col1, col2 = st.columns([3, 1])
    with col1:
        field = st.text_input("Enter your Field of Study / Subject Area:", placeholder="e.g. Cybersecurity, Machine Learning, Economics")
    with col2:
        st.write("") # Layout spacer
        st.write("") 
        if st.button("Discover Topics", use_container_width=True):
            if field:
                with st.spinner("Analyzing current trends..."):
                    suggestions = ai_service.generate_topics(field)
                    st.session_state['topic_suggestions'] = suggestions
            else:
                st.warning("Please enter a field of study.")
                
    if 'topic_suggestions' in st.session_state:
        st.markdown(st.session_state['topic_suggestions'])
        
    st.divider()
    
    st.subheader("🚀 Phase 2: Generate Research Package")
    selected_topic = st.text_input(
        "Enter your selected research topic:", 
        placeholder="e.g. The Impact of Quantum Computing on RSA Encryption"
    )
    
    if st.button("Generate Research Package", type="primary", use_container_width=True):
        if selected_topic:
            with st.spinner("Synthesizing research questions, literature review, and methodology..."):
                content = ai_service.generate_research_package(selected_topic)
                st.session_state['current_topic'] = selected_topic
                st.session_state['generated_content'] = content
                
                # Save automatically to DB
                db_manager.save_research(user['id'], selected_topic, content)
                st.success("Research Package generated and saved to your history!")
        else:
            st.warning("Please enter a research topic.")
            
    # Display Output & Export Options
    if 'generated_content' in st.session_state:
        st.divider()
        st.markdown(st.session_state['generated_content'])
        
        st.subheader("📥 Export Options")
        topic = st.session_state.get('current_topic', 'research')
        content = st.session_state.get('generated_content', '')
        
        exp_col1, exp_col2, exp_col3 = st.columns(3)
        
        with exp_col1:
            st.download_button(
                label="📄 Download Markdown (.md)",
                data=ExportService.export_to_markdown(content),
                file_name=f"{topic_slug(topic)}.md",
                mime="text/markdown",
                use_container_width=True
            )
        with exp_col2:
            st.download_button(
                label="📝 Download Word (.docx)",
                data=ExportService.export_to_docx(topic, content),
                file_name=f"{topic_slug(topic)}.docx",
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                use_container_width=True
            )
        with exp_col3:
            st.download_button(
                label="📕 Download PDF (.pdf)",
                data=ExportService.export_to_pdf(topic, content),
                file_name=f"{topic_slug(topic)}.pdf",
                mime="application/pdf",
                use_container_width=True
            )

def _render_history(db_manager: DatabaseManager, user: dict):
    """History section showing previous generations for this user."""
    st.subheader("📜 Saved Research History")
    history = db_manager.get_user_history(user['id'])
    
    if not history:
        st.info("You haven't generated any research packages yet.")
        return
        
    for item in history:
        record_id, topic, content, created_at = item
        local_time = utc_to_local(created_at)
        with st.expander(f"📌 {topic} — ({local_time})"):
            st.markdown(content)
            
            # Allow downloading past generations directly
            st.download_button(
                label="Download PDF for this report",
                data=ExportService.export_to_pdf(topic, content),
                file_name=f"{topic_slug(topic)}.pdf",
                mime="application/pdf",
                key=f"hist_pdf_{record_id}"
            )

def topic_slug(topic: str) -> str:
    """Helper to turn a title string into a clean filename."""
    return "".join([c if c.isalnum() else "_" for c in topic]).lower()[:30]