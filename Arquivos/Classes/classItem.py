from tkinter import *
from PIL import Image, ImageTk

class Item:
    def __init__(self, titulo, ano, tipo, disponib=True, idNum=0, descricao="Descrição não definida"):
        self._id = idNum
        self.ano = ano
        self.titulo = titulo
        self.tipo = tipo
        self.disponib = disponib
        self.estoque = 1
        self.capa = f"Arquivos/Capas/{self._id}.png"
        self.descricao = descricao

    def getId(self):
        return self._id

    def getDisponibilidade(self):
        """ Retorna os ícones e textos de disponibilidade com base no estoque """
        if self.estoque > 0:
            return "disponibilidadeTrue.png", "Disponível", "lime"
        else:
            return "disponibilidadeFalse.png", "Indisponível", "red"

    def infoItem(self, display, itenmSelecionado):
        global itemSelecionado
        itemSelecionado = self

        # Atualiza a disponibilidade com base no estoque
        self.disponib = self.estoque > 0
        iconeDisp, textDisp, corDisp = self.getDisponibilidade()

        # Remove os widgets anteriores do display
        for widget in display.winfo_children():
            widget.destroy()

        # Exibir título "Informações"
        info = Label(display, text="Informações", font=("Arial", 20, "bold"), 
                     background="#3c3d61", foreground="white")
        info.pack(pady=10)

        # Exibir imagem da capa
        try:
            img = Image.open(self.capa)
            img = img.resize((140, 200), Image.LANCZOS)
            capa = ImageTk.PhotoImage(img)
            capaLabel = Label(display, image=capa)
            capaLabel.image = capa  
            capaLabel.pack(side="left", padx=10, anchor="n")
        except FileNotFoundError:
            print(f"Imagem {self.capa} não encontrada.")

        # Exibir informações do item
        Label(display, text=self.titulo, font=("Arial", 18, "bold"), 
              background="#3c3d61", foreground="white", wraplength=230, justify="left").pack(pady=5, anchor="w")

        Label(display, text=f"Tipo: {self.tipo}", font=("Arial", 12),
              background="#3c3d61", foreground="white", justify="left").pack(pady=1, anchor="w")

        Label(display, text=f"Ano: {self.ano}", font=("Arial", 12),
              background="#3c3d61", foreground="white", justify="left").pack(pady=1, anchor="w")

        Label(display, text=f"Estoque: {self.estoque}", font=("Arial", 12),
              background="#3c3d61", foreground="white", justify="left").pack(pady=1, anchor="w")

        Label(display, text=f"Disponível: {textDisp}", font=("Arial", 12),
              background="#3c3d61", foreground=corDisp, justify="left").pack(pady=1, anchor="w")

        Label(display, text=f"Descrição: {self.descricao}", font=("Arial", 12),
              background="#3c3d61", foreground="white", wraplength=300, justify="left").place(x=10, y=270)
