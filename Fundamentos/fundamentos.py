# classe: define o molde de um objeto(conjunto de atributos
# e métodos) -> PascalCase

# objeto:é a instância da classe.

# atributos:São as características(variáveis) que os objeto classe terão

# método:são a funções que descrevem o comportamento dos objetos

# Herança:Uma classe pode herdar atributos e métodos de outra classe(chamada de classe pai ou classe base)

# Encapsulamento:É um conceito de ocultar detalhes internos de
# de um objeto e proteger os dados de acessos externos

# Polimosfismo:Diferentes classes podem ter métodos com o mesmo
# nome, mas com comportamento diferente.

# Abstração: Ocultar a complexidade dos detalhes internos,
# expõe apenas o que é necessário para o uso

""" POO: USAR UM SISTEMA SIMPLES DE CLASSIFICAR UM DESTINO COMO VIAGEM"""
class Viagem:
    def __init__(self, destino):
        self.destino = destino
        # sem metodo
viagem_0 = Viagem("Paris")
viagem_1 = Viagem("Chile")
viagem_2 = Viagem("Tailândia")
viagem_3 = Viagem("Londres")

# listar os destinos em uma lista para a escolha d destino:
lista_viagem = [
    viagem_0,
    viagem_1,
    viagem_2,
    viagem_3,
]

# pegar o nome do usuario:
usuario = input("Digite o seu nome: ")
print(f""" {usuario}, Temos 4 destinos disponiveis:
      0 - Paris
      1 - Chile
      2 - Tailãndia
      3 - Londres""")

# selecionar uma opção:
selecionado = int(input("Selecione o destino: "))
print(f"{usuario}, seu destino é:{lista_viagem[selecionado].destino}")
