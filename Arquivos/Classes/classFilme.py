from Classes.classItem import Item

class Filme(Item):
    tipo = "Filme" 

    def __init__(self, titulo, ano, tipo, disponib=True, idNum=0, descricao="Descrição não definida", duracao=0, genero="Gênero não definido", versao3d=False, diretor="Diretor não definido"):
        super().__init__(titulo, ano, Filme.tipo, disponib, idNum, descricao)
        self.versao3d = versao3d
        self.diretor = diretor
