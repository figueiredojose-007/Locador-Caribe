from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from lib import *
from Classes.classAdmin import Admin

usuarioLogado = lerArquivo("Arquivos/Informações/usuarioLogado")[0]
janela = Tk()
janela.geometry("480x220")
janela.title(f"Perfil de {usuarioLogado.username}")
janela["bg"] = "#1b1b33"
janela.resizable(False, False)
janela.attributes("-toolwindow",False)
janela.iconbitmap("Arquivos/Imagens/logoProjetoIco.ico")

framePrincipal = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
framePrincipal.place(x=10,y=10,width=460,height=200)

if isinstance(usuarioLogado,Admin) == True:
    adminPerms = True
    pfp = "Arquivos/Imagens/iconAdminGrande.png"
    usuarioTipo = "Admininstrador"
else:
    adminPerms = False
    pfp = "Arquivos/Imagens/iconClienteGrande.png"
    usuarioTipo = "Cliente"

fotoUsuario = PhotoImage(file=pfp)
labelUsuario = Label(framePrincipal,image=fotoUsuario)
labelUsuario.image = fotoUsuario
labelUsuario.pack(anchor="nw",padx=10,pady=10)
nomeUsuario = Label(framePrincipal,text=usuarioLogado.username,font=("Arial", 20, "bold"),background="#3c3d61", foreground="white")
nomeUsuario.place(x=120,y=10)
tipoUsuario = Label(framePrincipal,text=usuarioTipo,font=("Arial", 14),background="#3c3d61", foreground="white")
tipoUsuario.place(x=120,y=50)

if adminPerms == False:
    listaLocacoes = usuarioLogado.listaAlocacoes
    listaFinal = "Itens alocados:\n"
    listaFinal = ", ".join(item.titulo for item in listaLocacoes)
    listaUsuario = Label(framePrincipal,text=listaFinal,font=("Arial", 14),background="#3c3d61", foreground="white",wraplength=280,justify="left")
    listaUsuario.place(x=120,y=75)

botaoSair = Button(
    framePrincipal, text="Logoff", borderwidth=1, highlightbackground="white",
    highlightthickness=2, background="#1b1b33", foreground="white", width=12,
    font=("Arial", 10, "bold"), command=lambda: logoff(janela, usuarioLogado)
)

botaoSair.pack(anchor="w",padx=10)
botaoVoltar = Button(framePrincipal, text="Voltar", borderwidth=1, highlightbackground="white",
                          highlightthickness=2, background="#1b1b33", foreground="white", width=12,
                          font=("Arial", 10, "bold"), command=lambda: [janela.destroy(), subprocess.run(["python3","Arquivos/catalogo.py"])])
botaoVoltar.pack(anchor="w",padx=10,pady=5)

janela.mainloop()