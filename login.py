from PIL import Image, ImageTk
from tkinter import *

#colocando modo escuro na janela:



# função para validar login:
def validar_login():
    usuario = entradausuario.get()
    senha = entradasenha.get()

    if usuario == 'jose' and senha == '1234':
        result_login.configure(text='Login efetuado com sucesso!',text_color='green')
        
    
    
    else:
        result_login.configure(text='Usuário ou senha inválidos!',text_color= 'red')




#criando janela:
janela = Tk()
janela.title('Locadora Caribe')
janela.geometry('740x360')
janela.iconbitmap('Imagens/logoProjetoIco.ico')
janela.configure(background='#1b1b33')
janela.attributes('-toolwindow', False)
janela.resizable(False, False)


display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(width=720,height=340, x=10, y=10)




#colocando elementos da janela:
label = Label(display, text='Bem-vindo!', font=('Arial', 40, 'bold'), background='#3c3d61', foreground='white')
label.pack(pady=5)

campo_usuario = Label(display, text='Usuário:', font=('Arial', 20, 'bold'), background='#3c3d61', foreground='white')
campo_usuario.pack(pady=5)

entradausuario = Entry(display)
entradausuario.pack(pady=5)

campo_senha = Label(display, text='Senha:', font=('Arial', 20, 'bold'), background='#3c3d61', foreground='white')
campo_senha.pack(pady=5)
entradasenha = Entry(display, show='*')
entradasenha.pack(pady=5)


displaybotoes = Frame(janela,background="#3c3d61")
displaybotoes.place(width=140,height=30, x=299, y=260)



botao = Button(displaybotoes, text="Logar", borderwidth=1, highlightbackground="white", highlightthickness=2, 
                  background="#1b1b33", foreground="white", font=("Arial",10,"bold"))
botao.pack(pady=5, padx=5, side=LEFT)

botao2 = Button(displaybotoes, text="Cadastrar", borderwidth=1, highlightbackground="white", highlightthickness=2, 
                  background="#1b1b33", foreground="white", font=("Arial",10,"bold"))
botao2.pack(pady=5, padx=5, side=RIGHT)








arvore = PhotoImage(file="Imagens/arvoree.png")
displayLogo = Label(display,image=arvore,background="#3c3d61")
displayLogo.place(x=480, y=100)  # Ajuste os valores conforme necessário

arvore2 = PhotoImage(file="Imagens/arvoree.png")
displayLogo = Label(display,image=arvore2,background="#3c3d61")
displayLogo.place(x=35, y=100)  # Ajuste os valores conforme necessário










#loop:
janela.mainloop()
