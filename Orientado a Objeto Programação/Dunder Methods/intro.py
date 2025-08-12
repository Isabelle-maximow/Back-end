'''
Métodos Especiais (Dunder Methods) em Python:
Os métodos especiais (também chamados de "dunder methods"
porque têm double underscores __) são métodos pré-definidos em
Python que permitem que você personalize o comportamento
de objetos em situações específicas, como:
    Criação de objetos (__init__)
    Representação em string (__str__, __repr__)
    Operações matemáticas (__add__, __sub__)
    Comparação entre objetos (__eq__, __lt__)
    Tamanho de objetos (__len__)
    Acesso a elementos (__getitem__, __setitem__)
Eles são fundamentais para implementar comportamentos
intuitivos em classes personalizadas.
'''

class Operacao:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, num):
        return Operacao(self.x + num.x, self.y + num.y)
    # retornar resultao:
    def __str__(self):
        return f"Operação: ({self.x}, {self.y})"
# criar numero x e y para a adição:
p1 = Operacao(1,1)
p2 = Operacao(3,4)
soma = p1 = p1 
print(soma) #4,2

# COMPARAÇÃO:
# metodo especial pra comparação de objetos 
# __eq__ -> comparação de igualdade 
# __lt__ -> maior ou menor 
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    # metodo comprativo:
    def __eq__(self, numero):
        return self.nota == numero.nota
    def __lt__(self, numero):
        return self.nota < numero.nota
# criar dois alunos e comparar as notas:
aluno1 = Aluno("Fulamo", 8.5) 
aluno2 = Aluno("Ciclano", 5.6) 

print(aluno1 == aluno2) #false
print(aluno1 < aluno2) #false

'''
metodo para acessar elementos do objeto, como um dicionario
e uma lista, __getitem__ e __setitem__ 
permite acessar como o get e modificar com o set, usando o objeto com uma chave 
parecido como um dicionario: objeto[chave]
'''
class ListaPersonalizda:
    def __init__(self, elementos):
        self.elementos = elementos
    #acessar o item pelo indice:
    def __getitem__(self, indice):
        return self.elementos[indice] # retorna o indice do elemento
    # modificar o elemento:
    def __setitem__(self, indice, valor):
        self.elementos[indice] = valor # precido co dicionario

# criar uma lista no objeto:
lista = ListaPersonalizda([10,20,30,40,50])
# comportameto de uma lista e diionario:
print(lista[0])

# modificar:
lista[1] = 99 # 20 vira 99


'''__ca__ '''
