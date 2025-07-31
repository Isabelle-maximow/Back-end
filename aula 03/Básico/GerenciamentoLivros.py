"""
Biblioteca;
Sistema de gerenciamento de livro.
adicionar titulo, autor e ano da publicação;
exibir uma lista dos titulos.
"""

class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
    def detalhe(self):
        print("----------------------")
        print(f"TÍTULO: {self.titulo}")
        print(f"AUTOR: {self.autor}")
        print(f"ANO PUBLICADO: {self.ano}")
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
        # for para exibir na horizontal:
        for i in self.livros: # roda a lista livros
            i.detalhe() #metodo da outra classe (livro)

# criar os livros:
livro1 = Livro("Quarta Asa", "Rebecca Yarros", 2024)
livro2 = Livro("Jantar Secreto", "Raphael Montes", 2019)
livro3 = Livro("Jane Eyre", "Charllote Bronthe", 1820)
livro4 = Livro("Gente pobre", "Fiodor Dostoievsky", 1846)

# instancia biblioteca responsavel por add e listar:
biblioteca = Biblioteca() # subir a instancia - chamar ela 
biblioteca.add_livro(livro1)
biblioteca.add_livro(livro2)
biblioteca.add_livro(livro3)
biblioteca.add_livro(livro4)

# exibir os livros:
biblioteca.lista_livros()



