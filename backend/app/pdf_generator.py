from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os
import textwrap

def generate_pdf(repo: str, score: int, summary: str, roadmap: list):
    filename = f"{repo}_GitGrade_Report.pdf"
    safe_filename = filename.replace("/", "_")
    
    path = os.path.join("pdfs", safe_filename)
    os.makedirs("pdfs", exist_ok=True)
    
    c = canvas.Canvas(path, pagesize=A4)
    width, height = A4
    
    # --- Header ---
    c.setFillColorRGB(0.1, 0.1, 0.4) # Dark Blue
    c.setFont("Helvetica-Bold", 22)
    c.drawString(50, height - 60, "GitGrade AI Report")
    
    c.setFillColorRGB(0, 0, 0) # Black
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 90, f"Repository: {repo}")
    
    # --- Score Badge ---
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 120, f"Overall Score: {score}/100")
    
    # --- Summary Section ---
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 160, "Recruiter Summary:")
    
    c.setFont("Helvetica", 11)
    text = c.beginText(50, height - 180)
    
    # Wrap summary text
    wrapper = textwrap.TextWrapper(width=80) 
    wrapped_summary = wrapper.wrap(text=summary)
    
    for line in wrapped_summary:
        text.textLine(line)
    
    c.drawText(text)
    
    # --- Roadmap Section ---
    # Calculate Y position based on summary length
    current_y = height - 180 - (len(wrapped_summary) * 15) - 40
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, current_y, "Personalized Roadmap:")
    current_y -= 25
    
    c.setFont("Helvetica", 11)
    for step in roadmap:
        # Wrap roadmap items too
        wrapped_step = wrapper.wrap(f"- {step}")
        for line in wrapped_step:
            c.drawString(60, current_y, line)
            current_y -= 15
        current_y -= 5 # Space between items
        
        if current_y < 50: # New Page if simplified
            c.showPage()
            current_y = height - 50

    c.save()
    return path
