from lib import *
from tkinter import *
from tkinter import messagebox

class Usuário:
    def __init__(self,username,senha):
        self._id = 100 + len(lerArquivo("itensUsuarios"))
        self.username = username
        self._senha = senha

    def getId(self):
        return self._id
    
    def setId(self, novoId):
        self._id = novoId

    def getSenha(self):
        return self._senha

    def setSenha(self, novaSenha):
        self._senha = novaSenha