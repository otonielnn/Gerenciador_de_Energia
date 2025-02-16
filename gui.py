from tkinter import ttk
from ttkbootstrap import Style
from energia import salvando_dados_cadastro, carregar_dados, deletar_usuario, adicionar_item_usuario

estilo = Style(theme='superhero')
janela = estilo.master
janela.minsize(400, 300)

add_itens_aberto = False
cadastro_aberto = False
view_itens_aberto = False

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
    
    botao_cadastro = ttk.Button(global_frame_menu, text='Cadastrar Usuário', command=cadastro_janela)
    botao_cadastro.grid(row=0, column=0, pady=10)

    botao_remover_usuario = ttk.Button(global_frame_menu, text='Remover Usuário', command=lambda: deletar_usuario_selecionado(tabela))
    botao_remover_usuario.grid(row=0, column=1, pady=10)

    botao_add_itens_usuario = ttk.Button(global_frame_menu, text='Adicionar novo item ao usuário', command=adicionar_itens_janela)
    botao_add_itens_usuario.grid(row=1, column=0, pady=10)

    botao_ver_itens_usuario = ttk.Button(global_frame_menu, text='Ver itens do usuário',command=visualizar_itens_janela)
    botao_ver_itens_usuario.grid(row=1, column=1, pady=10)

    global tabela
    tabela = ttk.Treeview(global_frame_menu, columns=('Nome', 'Produção Kwh', 'Preço do kWh'))
    tabela.heading('#0', text='Nome')
    tabela.heading('#1', text='Produção Kwh')
    tabela.heading('#2', text='Preço do kWh')
    tabela.column('#0', width=200, anchor="center")
    tabela.column('#1', width=200, anchor="center")
    tabela.column('#2', width=200, anchor="center")
    tabela.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    global_frame_menu.pack(padx=10, pady=10, expand='yes')

    carregar_tabela(tabela)
    janela.mainloop()

def cadastro_janela():

    global cadastro_aberto
    if cadastro_aberto:
        return
    
    if add_itens_aberto or view_itens_aberto:
        return

    janela.title('Cadastro')
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

    botoes_frame = ttk.Frame(global_frame_cadastro)
    botoes_frame.grid(row=4, column=0, columnspan=2, pady=10)

    botao_cadastrar = ttk.Button(botoes_frame, text='Cadastrar', command=capturando_dados_formulario)
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
    
    janela.title('Itens do Usuário')
    
    item = tabela.item(selected_item)
    nome_usuario = item['text']

    frame_itens = ttk.Frame(janela)

    label_nome_item = ttk.Label(frame_itens, text='Nome do item:')
    label_nome_item.grid(row=0, column=0, padx=10, pady=10)

    entrada_nome_item = ttk.Entry(frame_itens, width=80)
    entrada_nome_item.grid(row=0, column=1, padx=10, pady=10)
    
    label_uso_energia = ttk.Label(frame_itens, text='Consumo em kWh:')
    label_uso_energia.grid(row=1, column=0, padx=10, pady=10)

    entrada_uso_energia = ttk.Entry(frame_itens, width=80)
    entrada_uso_energia.grid(row=1, column=1, padx=10, pady=10)

    def esconder_itens():
        global add_itens_aberto
        add_itens_aberto = False
        frame_itens.pack_forget()

    def capturando_dados_itens():
        nome_item = entrada_nome_item.get()
        uso_energia = entrada_uso_energia.get()
        adicionar_item_usuario(nome_usuario, [nome_item, uso_energia])
        esconder_itens()
        carregar_tabela(tabela)
        
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
    nome_usuario = item['text']

    view_itens_frame = ttk.Frame(janela)

    tabela_itens = ttk.Treeview(view_itens_frame, columns=('Nome', 'Consumo em kWh'))
    tabela_itens.heading('Nome', text='Nome', anchor='center')
    tabela_itens.heading('Consumo em kWh', text='Consumo em kWh', anchor='center')
    tabela_itens.column('Nome', width=200, anchor='center')
    tabela_itens.column('Consumo em kWh', width=200, anchor='center')

    tabela_itens["show"] = "headings"
    tabela_itens.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    dados = carregar_dados()
    total_consumo = 0
    for linha in dados:
        if linha[0] == nome_usuario:
            qtd_itens = len(linha) - 3
            item = linha
            for i in range(qtd_itens):
                nome_item = item[3+i][0]
                consumo_item = item[3+i][1]
                tabela_itens.insert('', 'end', values=(nome_item, consumo_item))
                total_consumo += float(linha[3+i][1])

    produção_kwh = float(item[1])
    preço_kwh = float(item[2])
    total_consumo_reais = (produção_kwh - total_consumo) * preço_kwh

    def esconder_view_itens():
        global view_itens_aberto
        view_itens_aberto = False
        view_itens_frame.pack_forget()
    
    label_total_consumo_kwh = ttk.Label(view_itens_frame, text=f'Total de Consumo: {total_consumo:.2f} kWh')
    label_total_consumo_kwh.grid(row=1, column=0, columnspan=2, pady=10, padx=20)

    label_total_consumo_reais = ttk.Label(view_itens_frame, text=f'Gasto em Reais: R${total_consumo_reais:.2f}')
    label_total_consumo_reais.grid(row=2, column=0, columnspan=2, pady=10, padx=20)

    botao_fechar_view_itens = ttk.Button(view_itens_frame, text='Fechar', command=esconder_view_itens)
    botao_fechar_view_itens.grid(row=3, column=0, columnspan=2, pady=10, padx=20)

    view_itens_frame.pack(padx=10, pady=10, expand='yes')

    view_itens_aberto = True
    janela.mainloop()