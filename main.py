from tkinter import *
from PIL import Image, ImageTk

from lib import *

# Classe de item
class Item:
    def __init__(self,idNum,titulo,ano,tipo,disponib=True):
        self._id = idNum
        self.ano = ano
        self.titulo = titulo
        self.tipo = tipo
        self.disponib = disponib
        self.estoque = 1
        self.capa = f"Capas/{self._id}.png"


    def getId(self):
        return self._id

global listaItens
listaItens = [
    Item(100, "Forza Horizon 5", "2021", "Jogo"),
    Item(101, "Esquadrão Suicida", "2016", "Filme"),
    Item(102, "The Witcher 3", "2015", "Jogo"),
    Item(103, "Interstellar", "2014", "Filme"),
    Item(104, "Red Dead Redemption 2", "2018", "Jogo"),
    Item(105, "Cyberpunk 2077", "2020", "Jogo"),
    Item(106, "Oppenheimer", "2023", "Filme"),
    Item(107, "The Last of Us Part II", "2020", "Jogo"),
    Item(108, "Duna", "2021", "Filme"),
    Item(109, "God of War Ragnarok", "2022", "Jogo"),
    Item(110, "Avatar: O Caminho da Água", "2022", "Filme"),
    Item(111, "Horizon Forbidden West", "2022", "Jogo"),
    Item(112, "John Wick 4", "2023", "Filme"),
    Item(113, "Spider-Man 2", "2023", "Jogo"),
    Item(114, "Guardiões da Galáxia Vol. 3", "2023", "Filme")
]


# Front-end ===============================================================================================================================================
janela = Tk()
janela.geometry("940x560")
janela.title("Locadora Caribe")
janela["bg"] = "#1b1b33"
janela.resizable(False, False)
janela.attributes("-toolwindow",False)
janela.iconbitmap("Imagens/logoProjetoIco.ico")

itemSelecionado = ""

display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(x=10,y=10,width=395,height=540)

if itemSelecionado == "":
    displayTexto = Label(display, text="Seja bem-vindo à \nLocadora Caribe!!", 
                         font=("Arial", 20, "bold"), background="#3c3d61", 
                         foreground="white")
    displayTexto.pack(pady=20, anchor="center")

    logo = PhotoImage(file="Imagens/logoProjeto.png")
    displayLogo = Label(display,image=logo,background="#3c3d61")
    displayLogo.pack(anchor="center")

    displayTextoMenor = Label(display, 
        text="A Locadora Caribe é um projeto desenvolvido por Caio Enzo Bessa de Oliveira e José Fernandes Figueirêdo Filho, sob a orientação do professor Ciro Daniel Gurgel de Moura, no Instituto Federal do Rio Grande do Norte (IFRN). Criado para simular a experiência de uma locadora moderna, permitindo o aluguel de jogos e filmes por meio de uma interface intuitiva e prática.\n\nSelecione um item para ver suas informações.",
        font=("Arial", 12), background="#3c3d61", foreground="white", 
        wraplength=370, justify="center") 
    displayTextoMenor.pack(pady=5,padx=10,side="bottom") 

listarItens(listaItens)
janela.mainloop()
