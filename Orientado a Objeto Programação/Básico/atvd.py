"""
Biblioteca;
criar uma lista de 10 livros, pedir o nome do usuario, listar os livros
para o emprestimo, fazer print do livro solicitado
"""

class Livro:
    def __init__(self, titulo):
        self.titulo = titulo

    def detalhe(self):
        print("----------------------")
        print(f"TÍTULO: {self.titulo}")
        print("----------------------")

class Biblioteca:
    def __init__(self):
        self.livros=[]  # lista vazia, para adicionar livros
    
    # metodo para add livro a lista:
    def add_livro(self, livro):
        self.livros.append(livro) # add livro a lista

    # metodo para exibir:
    def lista_livros(self):
        print("~~ Livros na Biblioteca ~~")
        print("Disponiveis para emprestimo:")
        # for para exibir na horizontal:
        for i, x in enumerate(self.livros, start = 1): # start para a lista começar em 1
            print(f"{i} - {x.titulo}") # enumerando aparecendo o titulo e o numero - x.titulo
    
    # metodo para pegar o livro escolhido 
    def selecionar_livro(self, indice):
        return self.livros[indice -1]


titulos = ["Quarta Asa","Jantar Secreto", "Jane Eyre",
           "Gente pobre", "Crime e Castigo", "Vidas Secas",
           "Hora da Estrela", "livro2", "livro3", "livro4"]

# criar instania e usar o metodo add_livro
biblioteca = Biblioteca() # subir a instancia - chamar ela 
# loop para quebrar a lista em linhas e add na lista do objt biblioteca
for i in titulos:
    biblioteca.add_livro(Livro(i))

# listar chamando o metodo listar - do objeto biblioteca:
biblioteca.lista_livros()

escolha = int(input("Digite o ID do livro que deseja: "))
# pegar o livro:
livro_escolhido = biblioteca.selecionar_livro(escolha)
print(f"Voce escolheu o {livro_escolhido.titulo}")

# class Emprestimo:
#     def __init__(self, escolher, nome):
#         self.escolher = escolher
#         self.nome = nome

#     def info(self):
#         print("----------------------")
#         print(f"NOME: {self.nome}")
#         print(f"LIVRO EMPRESTADO: {self.escolher}")
#         print("----------------------")

# nome = input("Digite o seu nome: ")
# livro = int(input("Digite o ID do livro que deseja: "))

# nome = Emprestimo(livro, nome)
# livro = Emprestimo(livro, nome)
# nome.info()
# livro.info()







