
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
janela.geometry('300x300')
janela.iconbitmap('Imagens/logoProjetoIco.ico')







#colocando elementos da janela:
label = Label(janela, text='Faça seu login')
label.pack(pady=5)

campo_usuario = Label(janela, text='Usuário:')
campo_usuario.pack(pady=5)

entradausuario = Entry(janela)
entradausuario.pack(pady=5)

campo_senha = Label(janela, text='Senha:')
campo_senha.pack(pady=5)
entradasenha = Entry(janela)
entradasenha.pack(pady=5)

botao = Button(janela, text='Entrar', command=validar_login)
botao.pack(pady=5)





#loop:
janela.mainloop()
