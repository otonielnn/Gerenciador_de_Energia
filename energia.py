import csv
import os

def salvar_usuario(user):
    with open('usuarios.csv', mode='a', newline='', encoding='UTF-8') as arquivo:
        escritor = csv.writer(arquivo)
        nome = user[0]
        cpf = user[1]
        data_nascimento = user[2]
        endereco = user[3]
        cidade = user[4]
        estado = user[5]
        preco = user[6]
        escritor.writerow([nome, cpf, data_nascimento, endereco, cidade, estado, preco])

def carregar_usuarios():
    dados = []
    if not os.path.exists('usuarios.csv'):
        with open('usuarios.csv', mode='w', newline='', encoding='UTF-8') as arquivo:
            pass
    with open('usuarios.csv', mode='r', newline='', encoding='UTF-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha:
                dados.append(linha)
        return dados

def deletar_usuario(cpf_usuario):
    dados = carregar_usuarios()
    with open('usuarios.csv', mode='w', newline='', encoding='UTF-8') as arquivo:
        escritor = csv.writer(arquivo)
        for linha in dados:
            if linha[1] != cpf_usuario:
                escritor.writerow(linha)

def salvar_item(item):
    with open('itens.csv', mode='a', newline='', encoding='UTF-8') as arquivo:
        escritor = csv.writer(arquivo)
        id_item = item[0]
        id_usuario = item[1]
        nome = item[2]
        marca = item[3]
        descricao = item[4]
        uso_energia = item[5]
        escritor.writerow([id_item, id_usuario, nome, marca, descricao, uso_energia])

def carregar_item():
    dados = []
    if not os.path.exists('itens.csv'):
        with open('itens.csv', mode='w', newline='', encoding='UTF-8') as arquivo:
            pass
    with open('itens.csv', mode='r', newline='', encoding='UTF-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dados.append(linha)
        return dados
    
def deletar_item(id_item):
    dados = carregar_usuarios()
    with open('itens.csv', mode='w', newline='', encoding='UTF-8') as arquivo:
        escritor = csv.writer(arquivo)
        for linha in dados:
            if linha[0] != id_item:
                escritor.writerow(linha)