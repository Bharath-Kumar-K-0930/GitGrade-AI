from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf(repo: str, score: int, summary: str, roadmap: list):
    filename = f"{repo}_GitGrade_Report.pdf"
    # Clean filename of slashes
    safe_filename = filename.replace("/", "_")
    
    path = os.path.join("pdfs", safe_filename)
    os.makedirs("pdfs", exist_ok=True)
    
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4

    # Title
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, height - 50, "GitGrade AI – Repository Report")

    # Info
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Repository: {repo}")
    c.drawString(50, height - 100, f"Score: {score}/100")
    
    # Summary
    c.drawString(50, height - 140, "Summary:")
    
    text_obj = c.beginText(50, height - 160)
    text_obj.setFont("Helvetica", 11)
    
    # Simple wrapping logic (very basic)
    words = summary.split()
    line = ""
    for word in words:
        if text_obj.getX() + c.stringWidth(line + word) > width - 100:
            text_obj.textLine(line)
            line = word + " "
        else:
            line += word + " "
    text_obj.textLine(line)
    c.drawText(text_obj)

    # Roadmap
    y_pos = height - 250
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_pos, "Personalized Roadmap:")
    y_pos -= 20
    
    c.setFont("Helvetica", 11)
    for step in roadmap:
        c.drawString(60, y_pos, f"- {step}")
        y_pos -= 20

    c.save()
    return path
