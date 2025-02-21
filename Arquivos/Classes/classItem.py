from tkinter import *
from PIL import Image, ImageTk

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
    
    def infoItem(self, display):
        global itemSelecionado
        itemSelecionado = self
        item = self
        
        # Removendo todos os widgets dentro do display antes de adicionar novos
        for widget in display.winfo_children():
            widget.destroy()

        # Exibir título do item
        tituloItem = Label(display, text="Informações", font=("Arial", 20, "bold"), 
                        background="#3c3d61", foreground="white")
        tituloItem.pack(pady=10)

        # Converter para PhotoImage
        img = Image.open(item.capa)
        img = img.resize((140, 200), Image.LANCZOS) 
        capa = ImageTk.PhotoImage(img)
        capaLabel = Label(display, image=capa)
        capaLabel.image = capa
        capaLabel.pack(anchor="nw",padx=10)