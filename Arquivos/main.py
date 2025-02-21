from tkinter import *
from PIL import Image, ImageTk
from lib import *
from Classes.classItem import Item
from Classes.classJogo import Jogo

global listaItens
listaItens = [
    Jogo("Forza Horizon 5", "2021", "Jogo", "Xbox/PC", "Playground Games", 100),
    Item("Esquadrão Suicida", "2016", "Filme", "Jogo", 101),
    Jogo("The Witcher 3", "2015", "Jogo", "Multiplataforma", "CD Projekt Red", 102),
    Item("Interstellar", "2014", "Filme", "Jogo", 103),
    Jogo("Red Dead Redemption 2", "2018", "Jogo", "Multiplataforma", "Rockstar Games", 104),
    Jogo("Cyberpunk 2077", "2020", "Jogo", "Multiplataforma", "CD Projekt Red", 105),
    Item("Oppenheimer", "2023", "Filme", "Jogo", 106),
    Jogo("The Last of Us Part II", "2020", "Jogo", "PlayStation", "Naughty Dog", 107),
    Item("Duna", "2021", "Filme", "Jogo", 108),
    Jogo("God of War Ragnarok", "2022", "Jogo", "PlayStation", "Santa Monica Studio", 109),
    Item("Avatar: O Caminho da Água", "2022", "Filme", "Jogo", 110),
    Jogo("Horizon Forbidden West", "2022", "Jogo", "PlayStation", "Guerrilla Games", 111),
    Item("John Wick 4", "2023", "Filme", "Jogo", 112),
    Jogo("Spider-Man 2", "2023", "Jogo", "PlayStation", "Insomniac Games", 113),
    Item("Guardiões da Galáxia Vol. 3", "2023", "Filme", "Jogo", 114)
]


# Front-end ===============================================================================================================================================
janela = Tk()
janela.geometry("940x560")
janela.title("Locadora Caribe")
janela["bg"] = "#1b1b33"
janela.resizable(False, False)
janela.attributes("-toolwindow",False)
janela.iconbitmap("Arquivos/Imagens/logoProjetoIco.ico")

itemSelecionado = ""

display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(x=10,y=10,width=395,height=540)

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

listarItens(listaItens, janela,display)
janela.mainloop()
