from reportlab.platypus import SimpleDocTemplate, Paragraph

def generar_certificado(nombre):
    doc = SimpleDocTemplate(f"{nombre}_certificado.pdf")

    content = []
    content.append(Paragraph(f"Certificado MENFA para {nombre}", None))

    doc.build(content)
Paragraph(f"Puntaje final: {score}", styles["Normal"])
