from collections import defaultdict # pip install collections-extended
from tika import parser  # pip install tika
from PyPDF2 import PdfFileWriter, PdfFileReader #pip install PyPDF2
from os import kill
import re # pip install regex
import os as path # pip install os-sys


# diretório do arquivo extraído
raw = parser.from_file(r'C:\Users\Isac\Documents\Development\test-zone\folha-de-ponto1.pdf')
text = raw['content']
print("Lendo arquivo...")
print('Aguarde...')
# Parâmetro do Regex para filtrar somente os funcionários e lotações correspondentes
lista_a_1 = re.findall(r"FUNCIONARIO\s[0-9].+", text)
lista = []
for i in lista_a_1:
    i = i.replace('FUNCIONARIO ', '')
    i = i.replace(" - ", "-")
    lista.append(i)
keys = defaultdict(list) # Define o objeto que armazenará os índices de cada elemento

# Percorre todos os elementos da lista:
for key, value in enumerate(lista):
    keys[value].append(key) # Adiciona o índice do valor na lista de índices
x = []

# Exibe o resultado da pesquisa:
for value in keys:
    if len(keys[value]) >= 1:
        x.append([value, keys[value]])
print("-----------------------Aguarde-------------------------------")
inputpdf = PdfFileReader(open(r'C:\Users\Isac\Documents\Development\test-zone\folha-de-ponto1.pdf', "rb"))

nomearq = ""  # Define o nome do arquivo como uma string

# Função que quebra o PDF com todos os parâmetros definidos no código
def create_pdf(namefunc, paginas):
    output = PdfFileWriter()
    for i in paginas:
        output.addPage(inputpdf.getPage(i))
    nomearq = namefunc+".pdf"
    print(nomearq+"---OK")
    with open(nomearq, "wb") as outputStream:
        output.write(outputStream)

print("\nIdentificando Paginas...\n")
print("Iniciando Quebra de arquivo...\n")

# Estrutura de repetição de quebra do arquivo
for i in x:
    pagina = i[1]
    nome = i[0]
    create_pdf(nome, pagina)

print("\nScript finalizado!")
exit()