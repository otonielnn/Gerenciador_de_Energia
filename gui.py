from tkinter import ttk
from ttkbootstrap import Style

estilo = Style(theme='superhero')
janela = estilo.master
janela.minsize(400, 300)

def menu_janela():
    janela.title('Gerenciador de Energia')

    global_frame = ttk.Frame(janela)
    
    botao_cadastro = ttk.Button(global_frame, text='Fazer Cadastro', command=cadastro_janela)
    botao_cadastro.grid(row=0, column=0, padx=30, pady=100)

    botao_dados_energia = ttk.Button(global_frame, text='Remover Cadastro')
    botao_dados_energia.grid(row=0, column=1, padx=10, pady=100)

    tabela = ttk.Treeview(global_frame, columns=('Nome', 'Consumo em kWh', 'Produção', 'Preço do kWh'))
    tabela.heading('#0', text='Nome')
    tabela.heading('#1', text='Consumo em kWh')
    tabela.heading('#2', text='Produção')
    tabela.heading('#3', text='Preço do kWh')
    tabela.column('#0', width=200)
    tabela.column('#1', width=200)
    tabela.column('#2', width=200)
    tabela.column('#3', width=200)
    tabela.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    global_frame.pack(padx=10, pady=10, fill='both', expand='yes')
    janela.mainloop()

def cadastro_janela():
    janela.title('Cadastro')

    global_frame = ttk.Frame(janela)

    label_nome = ttk.Label(global_frame, text='Digite seu Nome:')
    label_nome.grid(row=0, column=0, padx=10, pady=10)

    entrada_nome = ttk.Entry(global_frame)
    entrada_nome.grid(row=0, column=1, padx=10, pady=10)

    label_uso_energia = ttk.Label(global_frame, text='Digite sua Média de consumo em kWh:')
    label_uso_energia.grid(row=1, column=0, padx=10, pady=10)

    entrada_uso_energia = ttk.Entry(global_frame)
    entrada_uso_energia.grid(row=1, column=1, padx=10, pady=10)

    label_producao_energia = ttk.Label(global_frame, text='Digite sua Produção em kWh:')
    label_producao_energia.grid(row=2, column=0, padx=10, pady=10)

    entrada_producao_energia = ttk.Entry(global_frame)
    entrada_producao_energia.grid(row=2, column=1, padx=10, pady=10)

    label_preco_kwd = ttk.Label(global_frame, text='Digite o preco kWh:')
    label_preco_kwd.grid(row=3, column=0, padx=10, pady=10)

    entrada_preco_kwd = ttk.Entry(global_frame)
    entrada_preco_kwd.grid(row=3, column=1, padx=10, pady=10)

    botao_cadastrar = ttk.Button(global_frame, text='Cadastrar')
    botao_cadastrar.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    global_frame.pack(padx=10, pady=10, fill='both', expand='yes')

    janela.mainloop()

# cadastro_janela()
menu_janela()