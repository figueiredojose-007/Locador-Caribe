from Classes.classUsuario import Usuário
from lib import *

class Cliente(Usuário):
    def __init__(self, username, senha):
        super().__init__(username,senha)
        self._id = 100 + len(lerArquivo("Arquivos/Informações/itensUsuarios"))
        self._senha = senha
        self.listaAlocacoes = []
    
    def alocar(self, alocacao):
        self.listaAlocacoes.append(alocacao)
        adicionarAoArquivo([self],"usuarioLogado")

    def desalocar(self, alocacao):
        self.listaAlocacoes.remove(alocacao)
        adicionarAoArquivo([self],"usuarioLogado")



