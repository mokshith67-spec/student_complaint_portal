from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(data):
    styles = getSampleStyleSheet()
    pdf = SimpleDocTemplate("complaints_report.pdf")

    content = []

    for index, row in data.iterrows():
        content.append(Paragraph(f"Name: {row['Name']}", styles['Normal']))
        content.append(Paragraph(f"Roll: {row['Roll']}", styles['Normal']))
        content.append(Paragraph(f"Type: {row['Type']}", styles['Normal']))
        content.append(Paragraph(f"Priority: {row['Priority']}", styles['Normal']))
        content.append(Paragraph(f"Complaint: {row['Complaint']}", styles['Normal']))
        content.append(Paragraph(f"Status: {row['Status']}", styles['Normal']))
        content.append(Paragraph("------------------------------------------------", styles['Normal']))

    pdf.build(content)
