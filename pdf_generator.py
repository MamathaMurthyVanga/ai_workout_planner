from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_pdf(text, filename="Workout_Plan.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 50
    for line in text.split('\n'):
        c.drawString(50, y, line)
        y -= 15
    c.save()
