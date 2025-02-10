import csv
import os

def salvando_dados_cadastro(nome, producao, preco):
    with open('dados.csv', mode='a', newline='', encoding='UTF-8') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, producao, preco])

def carregar_dados():
    dados = []
    if not os.path.exists('dados.csv'):
        with open('dados.csv', mode='w', newline='', encoding='UTF-8') as arquivo:
            pass
    with open('dados.csv', mode='r', newline='', encoding='UTF-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
        return dados

def deletar_usuario(nome):
    dados = carregar_dados()
    with open('dados.csv', mode='w', newline='', encoding='UTF-8') as arquivo:
        escritor = csv.writer(arquivo)
        for linha in dados:
            if linha[0] != nome:
                escritor.writerow(linha)