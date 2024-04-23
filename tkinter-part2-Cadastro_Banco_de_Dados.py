import sqlite3
import tkinter as tk

#Use a extensão como .sqlite3 para visualizar com o SQLITE VIEWER pelo VSCode
conexao = sqlite3.connect('clientes.sqlite3')
c = conexao.cursor()

#Use os comandos SQL em maiúsculo para facilitar a identificação da linguagem
#Recomendo definir uma chave primária para a tabela
c.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        sobrenome TEXT,
        email TEXT,
        telefone TEXT
    )
""")

conexao.commit()
conexao.close()

janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela.geometry("330x350")

def cadastrar_cliente(nome_entry, sobrenome_entry, email_entry, telefone_entry):
    conexao = sqlite3.connect('clientes.sqlite3')
    c = conexao.cursor()

    dados = [nome_entry.get(), sobrenome_entry.get(), email_entry.get(), telefone_entry.get()]
    c.execute("INSERT INTO clientes (nome, sobrenome, email, telefone) VALUES (?,?,?,?)", dados)
    print("Cadastro Realizado!")
    
    conexao.commit()
    conexao.close()

#Precisava adicionar os Labels e os Grids para cada entrada
nome_label = tk.Label(janela, text="Nome")
nome_label.grid(column=0, row=0)
nome_entry = tk.Entry(janela, width=100)
nome_entry.grid(column=1, row=0)

sobrenome_label = tk.Label(janela, text="Sobrenome")
sobrenome_label.grid(column=0, row=1)
sobrenome_entry = tk.Entry(janela, width=100)
sobrenome_entry.grid(column=1, row=1)

email_label = tk.Label(janela, text="Email")
email_label.grid(column=0, row=2)
email_entry = tk.Entry(janela, width=100)
email_entry.grid(column=1, row=2)

telefone_label = tk.Label(janela, text="Telefone")
telefone_label.grid(column=0, row=3)
telefone_entry = tk.Entry(janela, width=100)
telefone_entry.grid(column=1, row=3)

cadastrar_button = tk.Button(janela, text="Cadastrar", command=lambda:cadastrar_cliente(nome_entry, sobrenome_entry, email_entry, telefone_entry))
cadastrar_button.grid(column=0, row=4)

janela.mainloop()