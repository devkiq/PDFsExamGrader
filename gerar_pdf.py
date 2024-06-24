from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def gerar_pdf_resultados(alunos, output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica", 12)

    for aluno in alunos:
        c.drawString(50, height - 50, f"Nome: {aluno['Nome']}")
        y_position = height - 70
        for i, resultado in enumerate(aluno['Correção']):
            c.drawString(50, y_position, f"Questão {i+1}: Resposta: {resultado['Resposta']} | Correta: {resultado['Correta']} | Resultado: {'Certa' if resultado['Resultado'] else 'Errada'}")
            y_position -= 20
        c.showPage()

    c.save()
