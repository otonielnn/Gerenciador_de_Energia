from tkinter import ttk
from ttkbootstrap import Style
from energia import salvando_dados_cadastro, carregar_dados, deletar_usuario

estilo = Style(theme='superhero')
janela = estilo.master
janela.minsize(400, 300)

itens_aberto = False
cadastro_aberto = False

def carregar_tabela(lista):
    for item in lista.get_children():
        lista.delete(item)

    dados = carregar_dados()
    for linha in dados:
        lista.insert('', 'end', text=linha[0], values=(linha[1], linha[2]))

def deletar_usuario_selecionado(lista):
    selected_item = lista.selection()
    if selected_item:
        item = lista.item(selected_item)
        nome = item['text']
        deletar_usuario(nome)
        carregar_tabela(lista)

def menu_janela():
    janela.title('Gerenciador de Energia')

    global_frame_menu = ttk.Frame(janela)
    
    botao_cadastro = ttk.Button(global_frame_menu, text='Fazer Cadastro', command=cadastro_janela)
    botao_cadastro.grid(row=0, column=0, pady=10)

    botao_remover_usuario = ttk.Button(global_frame_menu, text='Remover Cadastro', command=lambda: deletar_usuario_selecionado(tabela))
    botao_remover_usuario.grid(row=0, column=1, pady=10)

    botao_itens_usuario = ttk.Button(global_frame_menu, text='Itens do Usuário', command=itens_janela)
    botao_itens_usuario.grid(row=1, column=0, pady=10)

    global tabela
    tabela = ttk.Treeview(global_frame_menu, columns=('Nome', 'Produção', 'Preço do kWh'))
    tabela.heading('#0', text='Nome')
    tabela.heading('#1', text='Produção')
    tabela.heading('#2', text='Preço do kWh')
    tabela.column('#0', width=200, anchor="center")
    tabela.column('#1', width=200, anchor="center")
    tabela.column('#2', width=200, anchor="center")
    tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    global_frame_menu.pack(padx=10, pady=10, expand='yes')

    carregar_tabela(tabela)
    janela.mainloop()

def cadastro_janela():
    janela.title('Cadastro')

    global cadastro_aberto
    if cadastro_aberto:
        return

    global_frame_cadastro = ttk.Frame(janela)

    label_nome = ttk.Label(global_frame_cadastro, text='Digite seu Nome:')
    label_nome.grid(row=0, column=0, padx=10, pady=10)

    entrada_nome = ttk.Entry(global_frame_cadastro, width=80)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    label_producao_energia = ttk.Label(global_frame_cadastro, text='Digite sua Produção em kWh:')
    label_producao_energia.grid(row=2, column=0, padx=10, pady=10)

    entrada_producao_energia = ttk.Entry(global_frame_cadastro, width=80)
    entrada_producao_energia.grid(row=2, column=1, padx=10, pady=10)

    label_preco_kwd = ttk.Label(global_frame_cadastro, text='Digite o preco kWh:')
    label_preco_kwd.grid(row=3, column=0, padx=10, pady=10)

    entrada_preco_kwd = ttk.Entry(global_frame_cadastro, width=80)
    entrada_preco_kwd.grid(row=3, column=1, padx=10, pady=10)
    
    def esconder_cadastro():
        global cadastro_aberto
        cadastro_aberto = False
        global_frame_cadastro.pack_forget()

    def capturando_dados_formulario():
        nome = entrada_nome.get()
        producao_energia = entrada_producao_energia.get()
        preco_kwd = entrada_preco_kwd.get()
        salvando_dados_cadastro(nome, producao_energia, preco_kwd)
        esconder_cadastro()
        carregar_tabela(tabela)
        tabela.selection()

    botao_cadastrar = ttk.Button(global_frame_cadastro, text='Cadastrar', command=capturando_dados_formulario)
    botao_cadastrar.grid(row=4, column=1, pady=10)
    
    botao_fechar = ttk.Button(global_frame_cadastro, text='Fechar', command=esconder_cadastro)
    botao_fechar.grid(row=4, column=0, pady=10)

    global_frame_cadastro.pack(padx=10, pady=10, expand='yes')

    cadastro_aberto = True

    janela.mainloop()

def itens_janela():
    janela.title('Itens do Usuário')

    global itens_aberto
    if itens_aberto:
        return

    global_frame_itens = ttk.Frame(janela)

    label_nome_item = ttk.Label(global_frame_itens, text='Nome do item:')
    label_nome_item.grid(row=0, column=0, padx=10, pady=10)

    entrada_nome_item = ttk.Entry(global_frame_itens, width=80)
    entrada_nome_item.grid(row=0, column=1, padx=10, pady=10)
    

    label_uso_energia = ttk.Label(global_frame_itens, text='Consumo em kWh:')
    label_uso_energia.grid(row=1, column=0, padx=10, pady=10)

    entrada_uso_energia = ttk.Entry(global_frame_itens, width=80)
    entrada_uso_energia.grid(row=1, column=1, padx=10, pady=10)

    def esconder_itens():
        global itens_aberto
        itens_aberto = False
        global_frame_itens.pack_forget()

    botao_fechar = ttk.Button(global_frame_itens, text='Fechar', command=esconder_itens)
    botao_fechar.grid(row=2, column=0, pady=10)

    global_frame_itens.pack(padx=10, pady=10, expand='yes')

    itens_aberto = True

    janela.mainloop()