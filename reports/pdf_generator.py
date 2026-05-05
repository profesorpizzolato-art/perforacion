from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generar_reporte(data, filename="reporte.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Reporte MENFA", styles["Title"]))
    content.append(Paragraph(f"ROP: {data['rop']}", styles["Normal"]))
    content.append(Paragraph(f"HHP: {data['hhp']}", styles["Normal"]))

    doc.build(content)

    return filename
