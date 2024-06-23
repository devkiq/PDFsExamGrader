import pdfplumber  # Biblioteca para ler e extrair texto de PDFs
import csv

#Função para ler respostas de um PDF
def ler_respostas_pdf(pdf_path):
    respostas_alunos = [] # Lista para armazenar as respotas de cada aluno
    with pdfplumber.open(pdf_path) as pdf: # Abre o PDF usando o pdfplumber
        for page in pdf.pages: # Itera sobre cada página PDF
            text = page.extract_text() # Extrai o texto da página atual do pdf
            lines = text.split('\n') # Divide o texto em linhas
            nome = lines[0] # A primeira linha se considera o nome do aluno
            respostas = [] 
            for line in lines[4:]: # Itera sobre as linhas a partir da quinta linha (índice 4)
                resposta = limpar_resposta(line.split()[0])  # Extrai a primeira palavra da linha como resposta o .split separa todas as palavras da linha em uma lista.
                respostas.append(resposta) # Adiciona a resposta à lista de respostas do aluno
            respostas_alunos.append({'Nome': nome, 'Respostas': respostas})  # Adiciona as respostas do aluno à lista geral
    return respostas_alunos


# Função para limpar caracteres indevidos da respota
def limpar_resposta(resposta):
    return resposta.replace("_", "").strip()  # Remove underlines e espaços em branco

#Função para corrigir a prova
def corrigir_prova(respostas, gabarito):
    resultados = [] # Lista para armazenar os resultados da correção de cada questão
    for resposta, correta in zip(respostas, gabarito): # Itera sobre cada resposta e a corresponde no gabarito.
        resposta = limpar_resposta(resposta) # Limpa a respota antes de compará-la  
        correta = limpar_resposta(correta) # Limpa a respota correta 
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
