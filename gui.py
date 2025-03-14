from tkinter import ttk
from ttkbootstrap import Style
from energia import carregar_usuarios, deletar_usuario, salvar_usuario, carregar_item, salvar_item, deletar_item
import uuid

estilo = Style(theme='superhero')
janela = estilo.master
janela.minsize(400, 300)

add_itens_aberto = False
cadastro_aberto = False
view_itens_aberto = False

def carregar_tabela_itens(lista_itens, cpf_usuario):
    for item in lista_itens.get_children():
        lista_itens.delete(item)

    dados = carregar_item()
    total_consumo = 0
    for linha in dados:
        CPF_dono = linha[1]
        if CPF_dono == cpf_usuario:
            id_item = linha[0]
            cpf_usuario = linha[1]
            nome = linha[2]
            marca = linha[3]
            descricao = linha[4]
            consumo = int(linha[5])
            total_consumo += consumo
            lista_itens.insert('', 'end', text=id_item, values=(id_item, cpf_usuario, nome, marca, descricao, consumo))
    return total_consumo

def carregar_tabela_usuarios(lista):
    for item in lista.get_children():
        lista.delete(item)

    dados = carregar_usuarios()
    for linha in dados:
        nome = linha[0]
        cpf = linha[1]
        data_nascimento = linha[2]
        endereco = linha[3]
        cidade = linha[4]
        estado = linha[5]
        preco_kwh = linha[6]
        lista.insert('', 'end', text=cpf, values=(nome, cpf, data_nascimento, endereco, cidade, estado, preco_kwh))

def deletar_usuario_selecionado(lista):
    selected_item = lista.selection()
    if selected_item:
        item = lista.item(selected_item)
        nome = item['text']
        deletar_usuario(nome)
        carregar_tabela_usuarios(lista)

def menu_janela():
    janela.title('Gerenciador de Energia')

    global_frame_menu = ttk.Frame(janela)
    
    botao_cadastro = ttk.Button(global_frame_menu, text='Cadastrar Usuário', command=cadastro_janela)
    botao_cadastro.grid(row=0, column=0, pady=10)

    botao_remover_usuario = ttk.Button(global_frame_menu, text='Remover Usuário', command=lambda: deletar_usuario_selecionado(tabela))
    botao_remover_usuario.grid(row=0, column=1, pady=10)

    botao_add_itens_usuario = ttk.Button(global_frame_menu, text='Adicionar novo item ao usuário', command=adicionar_itens_janela)
    botao_add_itens_usuario.grid(row=1, column=0, pady=10)

    botao_ver_itens_usuario = ttk.Button(global_frame_menu, text='Ver itens do usuário',command=visualizar_itens_janela)
    botao_ver_itens_usuario.grid(row=1, column=1, pady=10)

    global tabela
    tabela = ttk.Treeview(global_frame_menu, columns=('Nome', 'CPF', 'Data de Nascimento', 'Endereço', 'Cidade', 'Estado', 'Preço'))
    tabela["show"] = "headings"
    tabela.heading('Nome', text='Nome')
    tabela.heading('CPF', text='CPF')
    tabela.heading('Data de Nascimento', text='Data de Nascimento')
    tabela.heading('Endereço', text='Endereço')
    tabela.heading('Cidade', text='Cidade')
    tabela.heading('Estado', text='Estado')
    tabela.heading('Preço', text='Preço')
    
    tabela.column('Nome', width=200, anchor="center")
    tabela.column('CPF', width=200, anchor="center")
    tabela.column('Data de Nascimento', width=200, anchor="center")
    tabela.column('Endereço', width=200, anchor="center")
    tabela.column('Cidade', width=200, anchor="center")
    tabela.column('Estado', width=200, anchor="center")
    tabela.column('Preço', width=200, anchor="center")
    tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    global_frame_menu.pack(padx=10, pady=10, expand='yes')

    carregar_tabela_usuarios(tabela)
    janela.mainloop()

def cadastro_janela():

    global cadastro_aberto
    if cadastro_aberto:
        return
    
    if add_itens_aberto or view_itens_aberto:
        return

    janela.title('Cadastro')
    global_frame_cadastro = ttk.Frame(janela)

    label_nome = ttk.Label(global_frame_cadastro, text='Nome:')
    label_nome.grid(row=0, column=0, padx=10, pady=10)

    entrada_nome = ttk.Entry(global_frame_cadastro, width=80)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    label_cpf = ttk.Label(global_frame_cadastro, text='CPF:')
    label_cpf.grid(row=2, column=0, padx=10, pady=10)

    entrada_cpf = ttk.Entry(global_frame_cadastro, width=80)
    entrada_cpf.grid(row=2, column=1, padx=10, pady=10)

    label_data_nascimento = ttk.Label(global_frame_cadastro, text='Data Nascimento:')
    label_data_nascimento.grid(row=3, column=0, padx=10, pady=10)

    entrada_data_nascimento = ttk.Entry(global_frame_cadastro, width=80)
    entrada_data_nascimento.grid(row=3, column=1, padx=10, pady=10)

    label_data_nascimento = ttk.Label(global_frame_cadastro, text='Data Nascimento:')
    label_data_nascimento.grid(row=3, column=0, padx=10, pady=10)

    entrada_data_nascimento = ttk.Entry(global_frame_cadastro, width=80)
    entrada_data_nascimento.grid(row=3, column=1, padx=10, pady=10)

    label_endereco = ttk.Label(global_frame_cadastro, text='Endereço:')
    label_endereco.grid(row=4, column=0, padx=10, pady=10)

    entrada_endereco = ttk.Entry(global_frame_cadastro, width=80)
    entrada_endereco.grid(row=4, column=1, padx=10, pady=10)

    label_cidade = ttk.Label(global_frame_cadastro, text='Cidade:')
    label_cidade.grid(row=5, column=0, padx=10, pady=10)

    entrada_cidade = ttk.Entry(global_frame_cadastro, width=80)
    entrada_cidade.grid(row=5, column=1, padx=10, pady=10)

    estados = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT", "PA", "PB", 
    "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"
    ]

    label_estado = ttk.Label(global_frame_cadastro, text='Estado:')
    label_estado.grid(row=6, column=0, padx=10, pady=10)

    entrada_estado = ttk.Combobox(global_frame_cadastro, values=estados, state='readonly')
    entrada_estado.grid(row=6, column=1, padx=10, pady=10)

    label_preco_kwh = ttk.Label(global_frame_cadastro, text='Digite o preco kWh:')
    label_preco_kwh.grid(row=7, column=0, padx=10, pady=10)

    entrada_preco_kwh = ttk.Entry(global_frame_cadastro, width=80)
    entrada_preco_kwh.grid(row=7, column=1, padx=10, pady=10)
    
    def esconder_cadastro():
        global cadastro_aberto
        cadastro_aberto = False
        global_frame_cadastro.pack_forget()

    def capturando_dados_usuario():
        nome = entrada_nome.get()
        cpf = entrada_cpf.get()
        data_nascimento = entrada_data_nascimento.get()
        endereco = entrada_endereco.get()
        cidade = entrada_cidade.get()
        estado = entrada_estado.get()
        preco_kwh = entrada_preco_kwh.get()
        user = [nome, cpf, data_nascimento, endereco, cidade, estado, preco_kwh]
        salvar_usuario(user)
        esconder_cadastro()
        carregar_tabela_usuarios(tabela)
        tabela.selection()

    botoes_frame = ttk.Frame(global_frame_cadastro)
    botoes_frame.grid(row=8, column=0, columnspan=2, pady=10)

    botao_cadastrar = ttk.Button(botoes_frame, text='Cadastrar', command=capturando_dados_usuario)
    botao_cadastrar.grid(row=0, column=1, padx=10)
    
    botao_fechar = ttk.Button(botoes_frame, text='Fechar', command=esconder_cadastro)
    botao_fechar.grid(row=0, column=0, padx=10)

    global_frame_cadastro.pack(padx=10, pady=10, expand='yes')

    cadastro_aberto = True

    janela.mainloop()

def adicionar_itens_janela():
    
    global add_itens_aberto
    if add_itens_aberto:
        return
    
    if cadastro_aberto or view_itens_aberto:
        return
    
    selected_item = tabela.selection()
    if not selected_item:
        return
    
    janela.title('Adicionar Item')
    
    item = tabela.item(selected_item)
    cpf_usuario = item['text']
    print(cpf_usuario)

    frame_itens = ttk.Frame(janela)

    label_nome_item = ttk.Label(frame_itens, text='Nome do item:')
    label_nome_item.grid(row=0, column=0, padx=10, pady=10)

    entrada_nome_item = ttk.Entry(frame_itens, width=80)
    entrada_nome_item.grid(row=0, column=1, padx=10, pady=10)

    label_marca_item = ttk.Label(frame_itens, text='Marca:')
    label_marca_item.grid(row=1, column=0, padx=10, pady=10)

    entrada_marca_item = ttk.Entry(frame_itens, width=80)
    entrada_marca_item.grid(row=1, column=1, padx=10, pady=10)

    label_descricao_item = ttk.Label(frame_itens, text='Descrição:')
    label_descricao_item.grid(row=2, column=0, padx=10, pady=10)

    entrada_descricao_item = ttk.Entry(frame_itens, width=80)
    entrada_descricao_item.grid(row=2, column=1, padx=10, pady=10)
    
    label_uso_energia = ttk.Label(frame_itens, text='Consumo em kWh:')
    label_uso_energia.grid(row=3, column=0, padx=10, pady=10)

    entrada_uso_energia = ttk.Entry(frame_itens, width=80)
    entrada_uso_energia.grid(row=3, column=1, padx=10, pady=10)

    def esconder_itens():
        global add_itens_aberto
        add_itens_aberto = False
        frame_itens.pack_forget()

    def capturando_dados_itens():
        id_item = str(uuid.uuid4())
        nome_item = entrada_nome_item.get()
        marca_item = entrada_marca_item.get()
        descricao_item = entrada_descricao_item.get()
        uso_energia = entrada_uso_energia.get()
        item = [id_item, cpf_usuario, nome_item, marca_item, descricao_item, uso_energia]
        salvar_item(item)
        esconder_itens()
        carregar_tabela_usuarios(tabela)
        esconder_itens()


    botoes_frame = ttk.Frame(frame_itens)
    botoes_frame.grid(row=4, column=0, columnspan=2, pady=10)

    botao_fechar = ttk.Button(botoes_frame, text='Fechar', command=esconder_itens)
    botao_fechar.grid(row=0, column=0, padx=10)

    botao_adicionar = ttk.Button(botoes_frame, text='Adicionar', command=capturando_dados_itens)
    botao_adicionar.grid(row=0, column=1, padx=10)

    frame_itens.pack(padx=10, pady=10, expand='yes')

    add_itens_aberto = True

    janela.mainloop()

def visualizar_itens_janela():
    global view_itens_aberto
    if view_itens_aberto:
        return
    
    if cadastro_aberto or add_itens_aberto:
        return
    
    selected_item = tabela.selection()
    if not selected_item:
        return
    
    janela.title('Visualizar Itens')
    
    item = tabela.item(selected_item)
    cpf_usuario = item['text']

    view_itens_frame = ttk.Frame(janela)

    tabela_itens = ttk.Treeview(view_itens_frame, columns=('Id', 'CPF_dono', 'Nome', 'Marca', 'Descricao', 'Consumo em kWh'))
    tabela_itens.heading('Id', text='Id', anchor='center')
    tabela_itens.heading('CPF_dono', text='CPF_dono', anchor='center')
    tabela_itens.heading('Nome', text='Nome', anchor='center')
    tabela_itens.heading('Marca', text='Marca', anchor='center')
    tabela_itens.heading('Descricao', text='Descricao', anchor='center')
    tabela_itens.heading('Consumo em kWh', text='Consumo em kWh', anchor='center')

    tabela_itens.column('Id', width=200, anchor='center')
    tabela_itens.column('CPF_dono', width=200, anchor='center')
    tabela_itens.column('Nome', width=200, anchor='center')
    tabela_itens.column('Consumo em kWh', width=200, anchor='center')
    tabela_itens.column('Marca', width=200, anchor='center')
    tabela_itens.column('Descricao', width=200, anchor='center')

    tabela_itens["show"] = "headings"
    tabela_itens.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    def carregar_usuario_por_cpf(cpf_usuario):
        dados = carregar_usuarios()
        for linha in dados:
            if linha[1] == cpf_usuario:
                return linha
        return None
    
    usuario = carregar_usuario_por_cpf(cpf_usuario)
    preco = float(usuario[6])
    
    total_consumo = carregar_tabela_itens(tabela_itens, cpf_usuario)

    label_soma_consumo = ttk.Label(view_itens_frame, text=f'Consumo Total em kWh: {total_consumo}')
    label_soma_consumo.grid(row=1, column=0, columnspan=2)   

    label_valor_total = ttk.Label(view_itens_frame, text=f'Valor total do kWh em Real: R${total_consumo*preco}')
    label_valor_total.grid(row=2, column=0, columnspan=2)   

    def esconder_view_itens():
        global view_itens_aberto
        view_itens_aberto = False
        view_itens_frame.pack_forget()

    botao_fechar_view_itens = ttk.Button(view_itens_frame, text='Fechar', command=esconder_view_itens)
    botao_fechar_view_itens.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

    '''
    botao_deletar_itens = ttk.Button(view_itens_frame, text='Deletar Item', command=lambda: deletar_item(id_item))    
    botao_deletar_itens.grid(row=4, column=0, columnspan=2, pady=10, padx=20)
    '''

    view_itens_frame.pack(padx=10, pady=10, expand='yes')

    view_itens_aberto = True
    janela.mainloop()

   