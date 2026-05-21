from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_report(username, risk, score):

    filename = f"static/reports/{username}_report.pdf"

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "CyberArena Threat Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    content = f"""
    User: {username}<br/>
    Threat Level: {risk}<br/>
    Threat Score: {score}/100
    """

    paragraph = Paragraph(
        content,
        styles['BodyText']
    )

    elements.append(paragraph)

    doc.build(elements)

    return filename