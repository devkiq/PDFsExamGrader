import pdfplumber  # Biblioteca para ler e extrair texto de PDFs
from reportlab.lib.pagesizes import letter  # Biblioteca para definir o tamanho das páginas do PDF a ser gerado
from reportlab.pdfgen import canvas  # Biblioteca para gerar PDFs

#Função para ler respostas de um PDF
def ler_respostas_pdf(pdf_path):
    respostas_alunos = [] # É uma lista para armazenar as respostas dos alunos
    with pdfplumber.open(pdf_path) as pdf: # Abre o PDF especificado pelo caminho
        for page in pdf.pages : # loop para cada página do pdf
            text = page.extract_text() # Extrai o texto da página
            lines = text.split('\n') # Divide o texto em linhas
            nome = lines[0] # Suposição de que a primeira linha tenha o nome do Aluno
            respostas = lines[4:] # Supondo que as respostas estejam nas linhas seguinte
            respostas_alunos.append({'Nome': nome, 'Respostas': respostas}) # Adiciona as respostas do aluno à lista
    return respostas_alunos # Retorna a lista com as respostas preenchidas

#Função para corrigir a prova
def corrigir_prova(respostas, gabarito):
    resultados = [] # Lista para armazenar os resultados da correção de cada questão
    for resposta, correta in zip(respostas, gabarito): # Itera sobre cada resposta e a corresponde no gabarito.
        correta = correta.strip() # Remove espaços em branco desnecessários da respota correta.
        resultado = {
            'Resposta': resposta.strip(), # Respota do aluno (removendo espaços em branco)
            'Correta': correta, # Respota Correta
            'Resultado': resposta.strip() == correta # Verifica se a resposta está correta.
        }
        resultados.append(resultado) # Adiciona o resultado da correção à lista
    return resultados

# Caminho para o gabarito e o PDF de respostas

gabarito = ['LM', 'LM', 'S', 'S', 'LM', 'S', 'LM', 'LM', 'S', 'LM', 'S', 'S', 'LM', 'S', 'LM', 'S', 'S', 'S', 'LM', 'LM', 'LM'] # Exemplo de gabarito.
pdf_path = 'C:/PROJETOS PROGRAMAÇÃO/Projeto Correção de Provas/.venv/test-answers.pdf' # Subtuí aqui pelo seu pdf

respostas_alunos = ler_respostas_pdf(pdf_path) # Lê as respotas do PDF
for aluno in respostas_alunos:
    aluno['Correção'] = corrigir_prova(aluno['Respostas'], gabarito) #Corrige as respostas de cada aluno

for aluno in respostas_alunos:
    print(f"Nome: {aluno['Nome']}")
    for resultado in aluno['Correção']:
        print(f"Resposta: {resultado['Resposta']} | Correta: {resultado['Correta']} | Resultado: {resultado['Resultado']}")
