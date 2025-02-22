from tkinter import *
from PIL import Image, ImageTk

class Item:
    def __init__(self,titulo,ano,tipo,disponib=True,idNum=0):
        self._id = idNum
        self.ano = ano
        self.titulo = titulo
        self.tipo = tipo
        self.disponib = disponib
        self.estoque = 1
        self.capa = f"Arquivos/Capas/{self._id}.png"


    def getId(self):
        return self._id
    
    def infoItem(self, display, intemSelecionado):
        global itemSelecionado
        itemSelecionado = self
        item = self
        
        # Removendo todos os widgets dentro do display antes de adicionar novos
        for widget in display.winfo_children():
            widget.destroy()

        # Exibir o nome informação
        info = Label(display, text="Informações", font=("Arial", 20, "bold"), 
                        background="#3c3d61", foreground="white")
        info.pack(pady=10)

        img = Image.open(item.capa)
        img = img.resize((140, 200), Image.LANCZOS) 
        capa = ImageTk.PhotoImage(img)
        capaLabel = Label(display, image=capa)
        capaLabel.image = capa  
        capaLabel.pack(side="left", padx=10,anchor="n")  

        # Exibir info dos itens: nome, tipo, ano, estoque e disponibilidade
        nome = Label(display, text=item.titulo, font=("Arial", 16, "bold"), 
                        background="#3c3d61", foreground="white", wraplength=230, justify="left")
        nome.pack(pady=10, anchor="w")
        
        tipo = Label(display, text=f"Tipo: {item.tipo}", font=("Arial", 12),
                        background="#3c3d61", foreground="white", justify="left")
        tipo.pack(pady=5, anchor="w")
        ano = Label(display, text=f"Ano: {item.ano}", font=("Arial", 12),
                        background="#3c3d61", foreground="white", justify="left")
        ano.pack(pady=5, anchor="w")
        
        estoque = Label(display, text=f"Estoque: {item.estoque}", font=("Arial", 12),
                        background="#3c3d61", foreground="white", justify="left")
        estoque.pack(pady=5, anchor="w")
        
        disponibilidade = Label(display, text=f"Disponível: {item.disponib}", font=("Arial", 12),
                        background="#3c3d61", foreground="white", justify="left")
        disponibilidade.pack(pady=5, anchor="w")
        
