from animal import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca=raca
        
    def setRaca(self, racas):
        self.raca=racas
    def getRaca(self):
        return self.__raca
    def mostrar(self):
        return (f"Tipo: Gato, Nome: {self.getNome()}, Idade: {self.getIdade()}, Raça: {self.getRaca()}")

#g = Gato("Milito", 3, "Labrador")
#print(g.mostrar())
