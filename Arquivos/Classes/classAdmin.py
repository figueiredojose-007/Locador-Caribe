from Classes.classUsuario import Usuário
from lib import *

class Admin(Usuário):
    def __init__(self,username,senha):
        super().__init__(username,senha)
        self._id = 100 + len(lerArquivo("itensUsuarios"))
        self.username = username
        self.senha = senha
        self.listaAlocacoes = []

    def adicionarEstoque(self,item,listaItens):
        item.estoque += 1
        if item.estoque > 0:
            item.disponib = True
        adicionarAoArquivo(listaItens,"itensCatalogo")

    def removerEstoque(self,item,listaItens):
        item.estoque -= 1
        if item.estoque <= 0:
            item.estoque = 0
            item.disponib = False
        adicionarAoArquivo(listaItens,"itensCatalogo")


