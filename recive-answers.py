import csv #Manipulação de arquivos CSV
import pdfplumber  #Library para ler PDF

#Função para ler respostas de um PDF
def ler_respostas_pdf(pdf_path):
    respostas_alunos = [] # É uma lista para armazenar as respostas dos alunos
    with pdfplumber.open(pdf_path): # Abre o PDF especificado pelo caminho
        for page in pdf.pages: # loop para cada página do pdf
            text = page.extract_text() # Extrai o texto da página
            lines = text.split('\n') # Divide o texto em linhas
            nome = lines[0] # Suposição de que a primeira linha tenha o nome do Aluno
            respostas = lines[1:] # Supondo que as respostas estejam nas linhas seguinte
            respostas_alunos.append({'Nome': nome, 'Respostas': respotas}) # Adiciona as respostas do aluno à lista
            





# Caminho para o gabarito e o PDF de respostas

gabarito = ['A','B','C','D','E'] # Exemplo de gabarito.
pdf_path = 'Caminho do pdf.pdf' # Subtuí aqui pelo seu pdf
