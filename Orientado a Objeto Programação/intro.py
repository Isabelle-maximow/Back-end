"""
conceito de MVC ( modelo, visão e controlador) para desenvolver uma aplicação web:
Model(modelo) representa os dados / manipulação de dados 
View(visão) exibir dados para o usuario / front-end
Controller (controlador) parte logica do sistema / intermediario entre model e view /  back-end

projeto = desenvolvimento de sistema:
model =  sqlite e mariadb
view = javascript
controller = FastAPI 

~~~ NÃO ESQUECER DO CRUD ~~~
create, read, update, delet.

"""

'''
POO = Class
PascalCase= 1° letra maiuscula

snake_case= utiliza o underline (_) para_separar_palavras_entre_elas
cARMELcASE= 1° letra minuscula

Componentes principais da POO em Python:
classe: define o molde de um objeto(conjunto de atributos
e métodos) -> PascalCase
objeto:é a instância da classe.
atributos:São as características(variáveis) que os objetos da
classe terão
método:são a funções que descrevem o comportamento dos objetos
Herança:Uma classe pode herdar atributos e métodos de outra
classe(chamada de classe pai ou classe base)
Encapsulamento:É um conceito de ocultar detalhes internos de
de um objeto e proteger os dados de acessos externos
Polimosfismo:Diferentes classes podem ter métodos com o mesmo
nome, mas com comportamento diferente.
Abstração: Ocultar a complexidade dos detalhes internos,
expõe apenas o que é necessário para o uso
'''

# sintaxe basica do def 
def nome_função():
    pass

# sintaxe básica objeto:
class NomeDaClasse: # nome do objeto
    pass

"""
definir uma classe, definir os atributos da classe e o metodo da classe 
"""
class Nome: #uma instância 
    # metodo construtor, iniciar os atributos 
    # primeiro metodo chama de __init__
    def __init__(self, atributo1, atributo2): 
        # atributos, sempre o primeiro atrubuto é o self -> função de fazer uma ponte entre variaveis
       
       # definir o atributo:
       self.atributo1 = atributo1 
       self.atributo2 = atributo2 

    def metodo(self):
       print(f"Chamando o atributo1: {self.atributo1}")
       print(f"Chamando o atributo2: {self.atributo2}")
       
# consumir o objeto:
objeto = Nome("atributo1/ pink car", "atributo2/ blue car")
# chamar o objeto:
objeto.metodo()

# cirando objeto//class pessoa:
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        pass # executar programa independente do erro

    # definir o metodo que a ação 
    def apresentar(self):
        print(f"Olá, meu nome é: {self.nome}") 
        print(f"Minha idade é: {self.idade}") 

# criar a variavel do objeto:
pessoa = Pessoa("Maria", 30)
# chama a ação = metodo (def)
pessoa.apresentar()

"""
objeto é uma classe, essa classe tem uma instancia
atributos são as caracteristicas do objeto. | o método são as funções que descreve o comportamneot do objeto.
 
"""