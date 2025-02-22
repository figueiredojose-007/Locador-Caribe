from lib import *

class Usuário:
    def __init__(self,username,senha):
        self._id = 100 + len(lerArquivo("itensUsuarios"))
        self.username = username
        self.senha = senha