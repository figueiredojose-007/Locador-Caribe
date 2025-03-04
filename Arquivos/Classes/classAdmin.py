from Classes.classUsuario import Usuário
from lib import *
from tkinter import messagebox

class Admin(Usuário):
    def __init__(self,username,senha):
        super().__init__(username,senha)
        self._id = 100 + len(lerArquivo("itensUsuarios"))
        self.username = username
        self.senha = senha
        self.listaAlocacoes = "Admins não alocam itens."

    def adicionarCatalogo(self, item):
        listaDeItens = lerArquivo("Arquivos/Informações/itensCatalogo")
        index = next((i for i, obj in enumerate(listaDeItens) if obj.titulo == item.titulo), -1)
        if index != -1:
            listaDeItens[index].estoque += 1
            item.estoque += 1
            adicionarAoArquivo(listaDeItens, "itensCatalogo")
            messagebox.showinfo("Locadora Caribe", "Unidade adicionada.")
        else:
            messagebox.showerror("Erro", "Item não encontrado no catálogo.")
        
        if item.estoque == 0:
            item.disponib = False
        else:
            item.disponib = True
         
    def removerCatalogo(self, item):
        listaDeItens = lerArquivo("Arquivos/Informações/itensCatalogo")
        index = next((i for i, obj in enumerate(listaDeItens) if obj.titulo == item.titulo), -1)
        if index != -1:
            if item.estoque > 0:
                listaDeItens[index].estoque -= 1
                item.estoque -= 1
                adicionarAoArquivo(listaDeItens, "itensCatalogo")
                messagebox.showinfo("Locadora Caribe", "Unidade removida.")
            else:
                messagebox.showerror("Locadora Caribe", "Item indisponível")
            
            if item.estoque == 0:
                item.disponib = False
                listaDeItens[index].disponib = False
            else:
                item.disponib = True
                listaDeItens[index].disponib = True
        else:
            messagebox.showerror("Erro", "Item não encontrado no catálogo.")