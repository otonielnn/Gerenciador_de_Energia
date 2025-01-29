import csv

def salvando_dados_cadastro(nome, consumo, producao, preco):
    with open('dados.csv', mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, consumo, producao, preco])

def carregar_dados():
    dados = []
    with open('dados.csv', mode='r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
        return dados

def deletar_usuario(nome):
    dados = carregar_dados()
    with open('dados.csv', mode='w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for linha in dados:
            if linha[0] != nome:
                escritor.writerow(linha)