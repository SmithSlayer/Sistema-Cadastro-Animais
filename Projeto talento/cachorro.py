from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte=porte
        
    def setPorte(self, porte):
        self.__porte=porte
    def getPorte(self):
        return self.__porte
    def mostrar(self):
        return (f"Tipo: Cachorro, Nome: {self.getNome()}, Idade: {self.getIdade()}, Porte: {self.getPorte()}")

#c = Cachorro("Ati", 15, "Médio")
#print(c.mostrar()) 