# exemplo simples criando objeto 
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    # definir os metodos:
    def info(self):
        print(f"O modelo do carro é: {self.modelo}")
        print(f"O ano do carro é: {self.ano}")
        print(f"O marca do carro é: {self.marca}")

# chamar a instancia carro:
carro1 = Carro("Ford", "Mutang", 57)
carro2 = Carro("Ford", "Mutang", 27)
carro3 = Carro("Ford", "Mutang", 87)
carro1.info()
carro2.info()
carro3.info()