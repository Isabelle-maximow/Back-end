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
        self.clientes.append(add_nome, add_tell)
        
#add_nome = input("Insira o nome do cliente: ")
#add_tell = input("Insira o telefone do cliente: ")
#informaçoes = Sistema_Clientes(add_nome, add_tell)        
#'informaçoes.exibir()

class Lista:
    def __init__(self):
        pass
    def mostrar_lista(self):
        print("Lista de Clientes cadastrados")
        for i, x in enumerate(self.clientes, star = 1):
            print(f"{i} - {x.nome} | {x.telefone}")

# MENU
def menu():
    while True:
        escolha = int(input(''' MENU DE OPÇÕES 
                    1 - Adicionar clientes
                    2 - Visualizar lista de clientes
                    3 - Sair
                    Insira o ID do que deseja fazer: '''))
        if escolha == 1:
            add_nome = input("Insira o nome do cliente: ")
            add_tell = input("Insira o telefone do cliente: ")
            informaçoes = Sistema_Clientes(add_nome, add_tell)        
            informaçoes.exibir()
        elif escolha == 2:
            Lista()
        elif escolha == 3:
            print("Encerrando...")
            break
        else:
            print("Escolha uma opção válida")

menu()
with open ("clientes.txt", "w" ) as arquivo:
    for item in arquivo:
                arquivo.write(str(item) + "\n")