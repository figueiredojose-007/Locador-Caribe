from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
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
        
# Kitar da conta atual e liberar o espaço        
def logoff(janela, usuarioLogado):
    messagebox.showinfo("Locadora Caribe", "Desconectado com sucesso.")
    listaUsuarios = lerArquivo("Arquivos/Informações/itensUsuarios")
    for i, usuario in enumerate(listaUsuarios):
        if usuario.getId() == usuarioLogado.getId():
            listaUsuarios[i] = usuarioLogado  
    adicionarAoArquivo(listaUsuarios, "itensUsuarios")
    adicionarAoArquivo([], "usuarioLogado")
    janela.destroy()
    subprocess.run(["python3", "Arquivos/login.py"])

def listarItens(lista, janela, display, itemSelecionado, adminPerms=False, usuarioLogado=""):
    # Verifica se já existe uma scrollbar e remove antes de criar uma nova
    if hasattr(janela, "scrollbar") and janela.scrollbar.winfo_exists():
        janela.scrollbar.destroy()

    # Frame principal onde a lista será exibida
    frameLista = Frame(janela, width=500, height=197, background="#3c3d61")
    frameLista.place(x=415, y=50)

    # Canvas para exibir os itens
    listaShow = Canvas(frameLista, background="#3c3d61", width=500, height=536)
    listaShow.pack(side=LEFT, fill=BOTH, expand=True)

    # Criar e armazenar a scrollbar na janela para evitar múltiplas criações
    janela.scrollbar = Scrollbar(janela, orient="vertical", command=listaShow.yview)
    janela.scrollbar.pack(side=RIGHT, fill=Y)
    listaShow.configure(yscrollcommand=janela.scrollbar.set)

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

        if item.estoque == 0:
            item.disponib = False
        else:
            item.disponib = True

        # Verificando a disponibilidade
        if item.disponib:
            iconeDisp = "disponibilidadeTrue.png"
            textDisp = "Disponível"
            corDisp = "lime"
        else:
            iconeDisp = "disponibilidadeFalse.png"
            textDisp = "Indisponível"
            corDisp = "red"

        # Imagem de disponibilidade
        status = PhotoImage(file=f"Arquivos/Imagens/{iconeDisp}")
        imagem = Label(frame, image=status, highlightthickness=0, background="#3c3d61")
        imagem.image = status
        imagem.pack(padx=3, pady=1, side="left")

        # Texto de disponibilidade
        textoimagem = Label(frame, text=textDisp, fg=corDisp, bg="#3c3d61", font=("Arial", 10, "bold"))
        textoimagem.pack(padx=3, pady=1, side="left")

        # Botão para ver o item selecionado
        botaoVer = Button(frame, text="Ver item", borderwidth=1, highlightbackground="white",
                          highlightthickness=2, background="#1b1b33", foreground="white",
                          font=("Arial", 10, "bold"), command=lambda item=item: item.infoItem(display, itemSelecionado, adminPerms, usuarioLogado, janela))
        botaoVer.pack(padx=3, pady=3, anchor="e")

    listaShow.update_idletasks()





# Ver perfil
def verPerfil(janela):
    janela.after(500, lambda: [janela.destroy(), subprocess.run(["python3","Arquivos/perfil.py"])])
    