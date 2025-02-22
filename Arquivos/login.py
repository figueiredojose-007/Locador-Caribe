from PIL import Image, ImageTk
from tkinter import *
from tkinter import messagebox
from lib import *
import os
from Classes.classCliente import Cliente
import time

# Cadastrando um usuário
def cadastrarUsuario(usuario, senha):
    if not usuario or not senha:
        messagebox.showwarning("Locadora Caribe", "Usuário e senha não podem estar vazios.")
        return

    if not os.path.exists("itensUsuarios.txt"):
        listaUsuarios = []
    else:
        listaUsuarios = lerArquivo("itensUsuarios.txt")
        if not listaUsuarios:
            listaUsuarios = [] 

    listaUsuarios.append(Cliente(usuario.strip(), senha.strip()))
    adicionarAoArquivo(listaUsuarios, "itensUsuarios.txt")
    messagebox.showinfo("Locadora Caribe", "Usuário cadastrado com sucesso.")

# Validando o login do usuário
def validarLogin():
    usuario = entradausuario.get().strip()
    senha = entradasenha.get().strip()

    if not os.path.exists("Informações/itensUsuarios.txt"):
        messagebox.showinfo("Locadora Caribe", "Login ou senha inválidos.")
        return
    listaUsuarios = lerArquivo("itensUsuarios")

    result = False
    for item in listaUsuarios:
        if item.username.strip() == usuario and item.senha.strip() == senha:
            result = True
            break

    if result:
        messagebox.showinfo("Locadora Caribe", "Login efetuado com sucesso.")
        janela.after(2000, lambda: [janela.destroy(), exec(open('Arquivos/main.py').read())])
    else:
        messagebox.showinfo("Locadora Caribe", "Login ou senha inválidos.")

# Criando janela:
janela = Tk()
janela.title('Locadora Caribe')
janela.geometry('740x360')
janela.iconbitmap('Arquivos/Imagens/logoProjetoIco.ico')
janela.configure(background='#1b1b33')
janela.resizable(False, False)

display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(width=720, height=340, x=10, y=10)

# Colocando elementos da janela:
label = Label(display, text='Bem-vindo!', font=('Arial', 40, 'bold'), background='#3c3d61', foreground='white')
label.pack(pady=5)

campo_usuario = Label(display, text='Usuário:', font=('Arial', 20, 'bold'), background='#3c3d61', foreground='white')
campo_usuario.pack(pady=5)
entradausuario = Entry(display)
entradausuario.pack(pady=5)

campo_senha = Label(display, text='Senha:', font=('Arial', 20, 'bold'), background='#3c3d61', foreground='white')
campo_senha.pack(pady=5)
entradasenha = Entry(display, show='*')
entradasenha.pack(pady=5)

displaybotoes = Frame(janela, background="#3c3d61")
displaybotoes.place(width=140, height=30, x=299, y=260)

botao = Button(displaybotoes, text="Logar", borderwidth=1, highlightbackground="white", highlightthickness=2, 
               background="#1b1b33", foreground="white", font=("Arial", 10, "bold"), command=validarLogin)
botao.pack(pady=5, padx=5, side=LEFT, anchor="n")

botao2 = Button(displaybotoes, text="Cadastrar", borderwidth=1, highlightbackground="white", highlightthickness=2, 
                background="#1b1b33", foreground="white", font=("Arial", 10, "bold"), 
                command=lambda: cadastrarUsuario(entradausuario.get(), entradasenha.get()))
botao2.pack(pady=5, padx=5, side=RIGHT, anchor="n")

arvore = PhotoImage(file="Arquivos/Imagens/arvoree.png")
displayLogo = Label(display, image=arvore, background="#3c3d61")
displayLogo.place(x=480, y=100)

arvore2 = PhotoImage(file="Arquivos/Imagens/arvoree.png")
displayLogo = Label(display, image=arvore2, background="#3c3d61")
displayLogo.place(x=35, y=100)

# loop:
janela.mainloop()
