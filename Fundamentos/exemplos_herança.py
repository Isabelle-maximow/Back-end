# exemplo simples de POO herança

# CLASSE PAI:
class Animal:
    def __init__(self, nome):
        self.nome = nome
    # definir a ação do metodo:
    def fazer_som(self):
        print(f"{self.nome} está fazendo som.")
    
# FIM DA CLASSE PAI

# SUBCLASS
class Dog(Animal): # subclass, herdando a classe animal (tp conectando elas)
    '''após herdar a classe pai, podemos chamar as funções (metodos)
    da classe pai'''
    def fazer_som(self):
        #return super().fazer_som()
        print(f"{self.nome} está latindo.")

# CLASSE FILHO:
cachorro=Dog("Max")
# ação do metodo:
cachorro.fazer_som()

'''
classes filhos:
gato = mia
cavalo = relincha
galinha = carcareja
'''

class Cat(Animal):
    def fazer_som(self):
        print(f"{self.nome} está miando")
gato = Cat("Liz")
gato.fazer_som()

class Horse(Animal):
    def fazer_som(self):
        print(f"{self.nome} está relinchando")
cavalo = Horse("Pé de pano")
cavalo.fazer_som()

class Chicken(Animal):
    def fazer_som(self):
        print(f"{self.nome} está carcarejando")
galinha = Chicken("galinha pintadinha")
galinha.fazer_som()