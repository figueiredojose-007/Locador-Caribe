
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
janela.geometry('740x460')
janela.iconbitmap('Imagens/logoProjetoIco.ico')
janela.configure(background='#1b1b33')
janela.attributes('-toolwindow', False)
janela.resizable(False, False)

display = Frame(janela, borderwidth=1, highlightbackground="white", highlightthickness=2, background="#3c3d61")
display.place(width=720,height=440, x=10, y=10)




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

botao = Button(display, text='Entrar', command=validar_login)
botao.pack(pady=5)





#loop:
janela.mainloop()
