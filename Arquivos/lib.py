from tkinter import *
from PIL import Image, ImageTk
import pickle
import os
import subprocess

# Escrever uma lista de coisas em um arquivo (itens do catálogo ou usuários)
def adicionarAoArquivo(lista, nomeArquivo):
    arquivo = open(f"Arquivos/Informações/{nomeArquivo}.txt","wb")
    pickle.dump(lista,arquivo)
    arquivo.close()

# Ler um arquivo e retornar em uma lista
def lerArquivo(nomeArquivo):
    if os.path.exists(f"{nomeArquivo}.txt") == False:
        print("Nada foi encontrado.")
        return []
    else:
        arquivo = open(f"{nomeArquivo}.txt","rb")
        listaFinal = pickle.load(arquivo)
        arquivo.close()
        return listaFinal

usuarioLogado = lerArquivo("Arquivos/Informações/usuarioLogado")[0]
if type(usuarioLogado) != "<class 'Classes.classAdmin.Admin'>":
    adminPerms = True
    pfp = "Arquivos/Imagens/iconAdmin.png"
    usuarioTipo = "Admin"
else:
    adminPerms = False
    pfp = "Arquivos/Imagens/iconCliente.png"
    usuarioTipo = "Cliente"

# Listar todos os itens do catálogo em um scroller na parte direita da tela
def listarItens(lista, janela, display, itemSelecionado, adminPerms=False):
    # Frame principal onde a lista será exibida
    frameLista = Frame(janela, width=500, height=197, background="#3c3d61")
    frameLista.place(x=415, y=50)

    # Canvas para exibir os itens
    listaShow = Canvas(frameLista, background="#3c3d61",width=500,height=536)
    listaShow.pack(side=LEFT, fill=BOTH, expand=True)

    # Barra de rolagem
    scrollbar = Scrollbar(janela, orient="vertical", command=listaShow.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listaShow.configure(yscrollcommand=scrollbar.set)

    # Frame interno que conterá os itens
    frameItens = Frame(listaShow, background="#3c3d61")
    listaShow.create_window((0, 0), window=frameItens, anchor="nw", width=500)

    # Atualiza o tamanho do canvas conforme os itens são adicionados
    def ajustarScroll(event):
        listaShow.configure(scrollregion=listaShow.bbox("all"))

    frameItens.bind("<Configure>", ajustarScroll)

    for i, item in enumerate(lista):
        # Criando o frame de cada item
        frame = Frame(frameItens, borderwidth=1, highlightbackground="white", 
                      highlightthickness=2, background="#3c3d61")
        frame.pack(fill=X, padx=10, pady=10)
      
        # Título do item
        titulo = Label(frame, text=item.titulo, fg="white", bg="#3c3d61", font=("Arial", 18, "bold"))
        titulo.pack(padx=5, pady=1, anchor="w")

        # Ano e tipo do item
        textoSubtitulo = f"{item.tipo} - {item.ano}"
        subtitulo = Label(frame, text=textoSubtitulo, fg="white", bg="#3c3d61", font=("Arial", 12))
        subtitulo.pack(padx=5, pady=2, anchor="w")


        # Imagem de disponibilidade
        status = PhotoImage(file=f"Arquivos/Imagens/{item.iconeDisp}")
        imagem = Label(frame, image=status, highlightthickness=0, background="#3c3d61")
        imagem.image = status
        imagem.pack(padx=3, pady=1, side="left")

        # Texto de disponibilidade
        textoimagem = Label(frame, text=item.textDisp, fg=item.corDisp, bg="#3c3d61", font=("Arial", 10, "bold"))
        textoimagem.pack(padx=3, pady=1, side="left")

        # Frame para os botões
        frameBotoes = Frame(frame, background="#3c3d61")
        frameBotoes.pack(padx=3, pady=3, anchor="e")

        # Função para atualizar itemSelecionado antes de mostrar o item
        def atualizarEVer(item):
            itemSelecionado = item  
            item.infoItem(display, itemSelecionado)  

        # Botão "Ver item"
        botaoVer = Button(frameBotoes, text="Ver item", borderwidth=1, highlightbackground="white",
                        highlightthickness=2, background="#1b1b33", foreground="white",
                        font=("Arial", 10, "bold"),
                        command=lambda i=item: atualizarEVer(i))
        botaoVer.grid(row=0, column=0, padx=2)

        # Botão "+1"
        botaoAdd = Button(frameBotoes, text="+1", borderwidth=1, highlightbackground="white", 
                        highlightthickness=2, background="#1b1b33", foreground="white",
                        font=("Arial", 10, "bold"), 
                        command=lambda i=item: [usuarioLogado.adicionarEstoque(i, lista), atualizarEVer(i)])
        botaoAdd.grid(row=0, column=1, padx=2)

        # Botão "-1"
        botaoRem = Button(frameBotoes, text="-1", borderwidth=1, highlightbackground="white", 
                        highlightthickness=2, background="#1b1b33", foreground="white",
                        font=("Arial", 10, "bold"), 
                        command=lambda i=item: [usuarioLogado.removerEstoque(i, lista), atualizarEVer(i)])
        botaoRem.grid(row=0, column=2, padx=2)

    listaShow.update_idletasks()

# Ver perfil
def verPerfil(janela):
    janela.after(500, lambda: [janela.destroy(), subprocess.run(["python3","Arquivos/perfil.py"])])
    