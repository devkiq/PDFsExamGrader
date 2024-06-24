import os
import pdfplumber
from gerar_pdf import gerar_pdf_resultados

# Função para limpar caracteres indevidos da resposta
def limpar_resposta(resposta):
    return resposta.replace("_", "").strip()

# Função para ler respostas de um PDF
def ler_respostas_pdf(pdf_path):
    respostas_alunos = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split('\n')
            nome = lines[0]
            respostas = []
            for line in lines[4:]:
                resposta = limpar_resposta(line.split()[0])
                respostas.append(resposta)
            respostas_alunos.append({'Nome': nome, 'Respostas': respostas})
    return respostas_alunos

# Função para corrigir a prova
def corrigir_prova(respostas, gabarito):
    resultados = []
    for resposta, correta in zip(respostas, gabarito):
        resposta = limpar_resposta(resposta)
        correta = limpar_resposta(correta)
        resultado = {
            'Resposta': resposta.strip(),
            'Correta': correta,
            'Resultado': resposta.strip() == correta
        }
        resultados.append(resultado)
    return resultados

# Caminho para o gabarito e o diretório de PDFs de respostas
gabarito = ['A','B','C','D','E']
pdf_directory = 'pdfs'
output_directory = 'resultados'

# Verifica se o diretório de saída existe, caso contrário, cria-o
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Itera sobre todos os arquivos PDF no diretório especificado
for pdf_file in os.listdir(pdf_directory):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, pdf_file)
        respostas_alunos = ler_respostas_pdf(pdf_path)
        for aluno in respostas_alunos:
            aluno['Correção'] = corrigir_prova(aluno['Respostas'], gabarito)
        
        # Define o caminho onde o PDF de resultados será salvo
        output_path = os.path.join(output_directory, f'resultado_{os.path.splitext(pdf_file)[0]}.pdf')
        
        # Gera o PDF com os resultados da correção
        gerar_pdf_resultados(respostas_alunos, output_path)
