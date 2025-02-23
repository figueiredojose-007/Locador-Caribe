from classUsuario import Usuário

class Admin(Usuário):
    def __init__(self,username,senha):
        super()
        self._id = 100 + len(lerArquivo("itensUsuarios"))
        self.username = username
        self.senha = senha