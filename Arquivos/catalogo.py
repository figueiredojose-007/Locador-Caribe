from tkinter import *
from PIL import Image, ImageTk
from lib import *
from Classes.classFilme import Filme
from Classes.classJogo import Jogo

# Verificando se o usuário é um admininstrador
usuarioLogado = lerArquivo("Arquivos/Informações/usuarioLogado")[0]
if type(usuarioLogado) == "<class 'Classes.classAdmin.Admin'>":
    adminPerms = True
else:
    adminPerms = False

# Lendo o arquivo que contém os itens do catálogo
global listaItens
adicionarAoArquivo(listaItens,"itensCatalogo")
listaItens = lerArquivo("Arquivos/Informações/itensCatalogo")

# Interface do projeto
janela = Tk()
janela.geometry("940x600")
janela.title(f"Locadora Caribe - {usuarioLogado.username}")
janela["bg"] = "#1b1b33"
janela.resizable(False, False)
janela.attributes("-toolwindow",False)
janela.iconbitmap("Arquivos/Imagens/logoProjetoIco.ico")

global itemSelecionado
itemSelecionado = ""

display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(x=10,y=50,width=395,height=540)

if itemSelecionado == "":
    displayTexto = Label(display, text="Seja bem-vindo à \nLocadora Caribe!!", 
                         font=("Arial", 20, "bold"), background="#3c3d61", 
                         foreground="white")
    displayTexto.pack(pady=20, anchor="center")

    logo = PhotoImage(file="Arquivos/Imagens/logoProjeto.png")
    displayLogo = Label(display,image=logo,background="#3c3d61")
    displayLogo.pack(anchor="center")

    displayTextoMenor = Label(display, 
        text="A Locadora Caribe é um projeto desenvolvido por Caio Enzo Bessa de Oliveira e José Fernandes Figueirêdo Filho, sob a orientação do professor Ciro Daniel Gurgel de Moura, no Instituto Federal do Rio Grande do Norte (IFRN). Criado para simular a experiência de uma locadora moderna, permitindo o aluguel de jogos e filmes por meio de uma interface intuitiva e prática.\n\nSelecione um item para ver suas informações.",
        font=("Arial", 12), background="#3c3d61", foreground="white", 
        wraplength=370, justify="center") 
    displayTextoMenor.pack(pady=5,padx=10,side="bottom",) 

janela.after(500, listarItens(listaItens, janela,display,itemSelecionado, adminPerms))
janela.mainloop()
