from Classes.classItem import Item

class Jogo(Item):
    tipo = "Jogo" 
    
    def __init__(self, titulo, ano, disponib, plataforma, desenvolvedora, id, descricao):
        super().__init__(titulo, ano, Jogo.tipo, disponib)  
        self._id = id
        self.plataforma = plataforma
        self.desenvolvedora = desenvolvedora
        self.estoque = 1
        self.capa = f"Arquivos/Capas/{self._id}.png"
        self.descricao = descricao
        
