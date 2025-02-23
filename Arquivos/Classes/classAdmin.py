from classUsuario import Usuário
from lib import *

class Admin(Usuário):
    def __init__(self,username,senha):
        super().__init__(username,senha)
        self._id = 100 + len(lerArquivo("itensUsuarios"))
        self.username = username
        self.senha = senha
