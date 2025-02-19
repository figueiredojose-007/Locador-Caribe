from tkinter import *
from PIL import Image, ImageTk

janela = Tk()
display = Frame(janela)

# Função de filtro de itens em uma lista
def filtrarItens(lista, tipoFiltro, filtro):                    # Recebe uma lista de itens, um atributo para filtrar e uma referência de filtro
    listaFinal = []                                             # Criação da lista final que é retornada no final
    if tipoFiltro == "titulo":                                  # Filtragem por título
        for item in lista:
            if item.titulo == filtro:
                listaFinal.append(item)

    elif tipoFiltro == "tipo":                                  # Filtragem por tipo
        for item in lista:
            if item.tipo == filtro:
                listaFinal.append(item)

    elif tipoFiltro == "ano":                                   # Filtragem por ano
        for item in lista:
            if item.ano == filtro:
                listaFinal.append(item)

    elif tipoFiltro == "disponib":                              # Filtragem por disponibilidade
        for item in lista:
            if item.disponib == filtro:
                listaFinal.append(item)

    return listaFinal

# Função de selecionar um item para o painel principal
def infoItem(item):
    global itemSelecionado
    itemSelecionado = item
    
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

    # Exibindo as informações do item

# Função de listar os itens na interface, sempre ao lado direito da tela
def listarItens(lista):                                         # Recebe uma lista de itens para mostrar
    for i, item in enumerate(lista):
        # Caixa de cada item
        frame = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
        frame.place(x=413, y=10 + 110 * i, width=500, height=100)

        # Título do item
        titulo = Label(frame, text=item.titulo, fg="white", bg="#3c3d61", font=("Arial", 18, "bold"))
        titulo.pack(padx=5,pady=1,anchor="w")
        
        # Ano e tipo do item
        textoSubtitulo = f"{item.tipo} - {item.ano}"
        subtitulo = Label(frame,text=textoSubtitulo,fg="white", bg="#3c3d61", font=("Arial", 12))
        subtitulo.pack(padx=5,pady=2,anchor="w")

        # Verificando e configurando a disponibilidade do item
        if item.disponib:
            iconeDisp = "disponibilidadeTrue.png"
            textDisp = "Disponível"
            corDisp = "lime"
        else:
            iconeDisp = "disponibilidadeFalse.png"
            textDisp = "Indisponível"
            corDisp = "red"
        
        # Imagem da bolinha
        status = PhotoImage(file=f"Imagens/{iconeDisp}")

        # Mostrando a imagem
        imagem = Label(frame,image=status,highlightthickness=0,background="#3c3d61")
        imagem.image = status
        imagem.pack(padx=3,pady=1,anchor="w",side="left")

        # Mostrando o texto de disponibilidade
        textoimagem = Label(frame,text=textDisp,fg=corDisp,bg="#3c3d61", font=("Arial",10,"bold"))
        textoimagem.pack(padx=3,pady=1,side="left")

        # Mostrando o botão de ver o item selecionado
        botaoVer = Button(frame, text="Ver item", borderwidth=1, highlightbackground="white", highlightthickness=2, 
                  background="#1b1b33", foreground="white", font=("Arial",10,"bold"), 
                  command=lambda item=item: infoItem(item))  

        botaoVer.pack(padx=3,pady=3,anchor="e")
    
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
