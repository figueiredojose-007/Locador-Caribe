class Cliente:
    def __init__(self, nome, idade,sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.listaAlocacoes = []
    
    def alocar(self, alocacao):
        self.listaAlocacoes.append(alocacao)

    def desalocar(self, alocacao):
        self.listaAlocacoes.remove(alocacao)

