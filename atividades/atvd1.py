'''
ALUNA: Isabelle Ferreira
RA: 24271526
DATA: 07/08/25
'''
class Sistema_Clientes:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
    def exibir(self):
        print("----------------------")
        print(f"NOME: {self.nome}")
        print(f"TELEFONE: {self.telefone}")
        print("----------------------")

class Adicionar_Cliente:
    def __init__(self):
        self.clientes = []
    def add_cliente(self, add_nome, add_tell):
        cliente = Sistema_Clientes(add_nome, add_tell)
        self.clientes.append(cliente)

    def mostrar_lista(self):
        print("Lista de Clientes cadastrados")
        if not self.clientes:
            print("Nenhum cliente cadastrado.")
        for i, x in enumerate(self.clientes, start=1):
            print(f"{i} - {x.nome} | {x.telefone}")

# MENU
def menu():
    sistema = Adicionar_Cliente()
    while True:
        escolha = int(input(''' MENU DE OPÇÕES 
                    1 - Adicionar clientes
                    2 - Visualizar lista de clientes
                    3 - Sair
                    Insira o indice do que deseja fazer: '''))
        if escolha == 1:
            add_nome = input("Insira o nome do cliente: ")
            add_tell = (input("Insira o telefone do cliente: "))
            sistema.add_cliente(add_nome, add_tell)
            print("Cliente adicionado com sucesso!")
        elif escolha == 2:
            sistema.mostrar_lista()
        elif escolha == 3:
            print("Encerrando...")
            # salvar clientes no arquivo ao sair
            with open("clientes.txt", "w") as arquivo:
                for cliente in sistema.clientes:
                    arquivo.write(f"{cliente.nome},{cliente.telefone}\n")
            break
        else:
            print("Escolha uma opção válida")

menu()