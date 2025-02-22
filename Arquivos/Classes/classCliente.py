from Classes.classUsuario import Usuário
from lib import *

class Cliente(Usuário):
    def __init__(self, username, senha):
        super().__init__(username,senha)
        self._id = 100 + len(lerArquivo("itensUsuarios"))
        self.listaAlocacoes = []
    
    def alocar(self, alocacao):
        self.listaAlocacoes.append(alocacao)

    def desalocar(self, alocacao):
        self.listaAlocacoes.remove(alocacao)

