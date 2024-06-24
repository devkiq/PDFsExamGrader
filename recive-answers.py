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

# Caminho para o gabarito e o PDF de respostas
gabarito = ['LM', 'LM', 'S', 'S', 'LM', 'S', 'LM', 'LM', 'S', 'LM', 'S', 'S', 'LM', 'S', 'LM', 'S', 'S', 'S', 'LM', 'LM', 'LM']
pdf_path = 'C:/PROJETOS PROGRAMAÇÃO/Projeto Correção de Provas/test-answers.pdf'

# Lê as respostas do PDF e corrige as provas
respostas_alunos = ler_respostas_pdf(pdf_path)
for aluno in respostas_alunos:
    aluno['Correção'] = corrigir_prova(aluno['Respostas'], gabarito)

# Define o caminho onde o PDF de resultados será salvo
output_path = 'C:/PROJETOS PROGRAMAÇÃO/Projeto Correção de Provas/resultados_correcao.pdf'

# Gera o PDF com os resultados da correção
gerar_pdf_resultados(respostas_alunos, output_path)
