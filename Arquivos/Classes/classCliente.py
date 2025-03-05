from Classes.classUsuario import Usuário
from lib import *

class Cliente(Usuário):
    def __init__(self, username, senha):
        super().__init__(username, senha)
        self._id = 100 + len(lerArquivo("Arquivos/Informações/itensUsuarios"))
        self._senha = senha
        self.listaAlocacoes = []

    @staticmethod
    def obterAdmin():
        listaUsuarios = lerArquivo("Arquivos/Informações/itensUsuarios")
        return listaUsuarios[0] if listaUsuarios else None

    def alocar(self, alocacao):
        if alocacao.disponib == True:
            self.listaAlocacoes.append(alocacao)
            adicionarAoArquivo([self], "usuarioLogado")
        adm = self.obterAdmin()
        if adm:
            adm.removerCatalogo(alocacao)
            

    def desalocar(self, alocacao):
        for item in self.listaAlocacoes:
            if item.titulo == alocacao.titulo:  # Comparação pelo título
                self.listaAlocacoes.remove(item)  # Removendo o objeto real
                adicionarAoArquivo([self], "usuarioLogado")
                
                adm = self.obterAdmin()
                if adm:
                    adm.adicionarCatalogo(alocacao)
                return  # Encerra a função após remover
        
        # Se não encontrar, exibe erro
        messagebox.showerror("Locadora Caribe", "Você não alocou este item")

