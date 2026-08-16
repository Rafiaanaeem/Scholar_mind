import io
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

class ExportService:
    """Handles converting Markdown text into downloadable files (MD, DOCX, PDF)."""

    @staticmethod
    def export_to_markdown(content: str) -> bytes:
        """Converts text to bytes for a .md file download."""
        return content.encode('utf-8')

    @staticmethod
    def export_to_docx(topic: str, content: str) -> bytes:
        """Generates a Microsoft Word document in memory."""
        doc = Document()
        doc.add_heading(f"Research: {topic}", 0)
        
        for line in content.split('\n'):
            if line.strip():
                if line.startswith('##'):
                    doc.add_heading(line.replace('##', '').strip(), level=2)
                else:
                    doc.add_paragraph(line)
                    
        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0) 
        return buffer.getvalue()

    @staticmethod
    def export_to_pdf(topic: str, content: str) -> bytes:
        """Generates a PDF document in memory using ReportLab."""
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter)
        styles = getSampleStyleSheet()
        flowables = []
        
        title = Paragraph(f"<b>Research: {topic}</b>", styles['Title'])
        flowables.append(title)
        flowables.append(Spacer(1, 12))
        
        for line in content.split('\n'):
            if line.strip():
                if line.startswith('##'):
                    p = Paragraph(f"<b>{line.replace('##', '').strip()}</b>", styles['Heading2'])
                else:
                    p = Paragraph(line, styles['Normal'])
                flowables.append(p)
                flowables.append(Spacer(1, 6))
                
        doc.build(flowables)
        buffer.seek(0)
        return buffer.getvalue()