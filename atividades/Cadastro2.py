# import mysql.connector

# CONFIG_BANCO = {
#     'host': 'localhost',
#     'user': 'root',
#     'password': 'dev1t@24',
#     'database': 'BANCO 02',
# }

# class Banco:
#     def __init__(self, config = CONFIG_BANCO):
#         self.config = config
#         self.conexao = mysql.connector.connect(**self.config)
#         self.cursor = self.conexao.cursor()
#         self.conectar_db()
        
#     def conectar_db(self):
#         self.cursor.execute('''CREATE TABLE IF NOT EXISTS aluno  (
#                         id INT AUTO_INCREMENT PRIMARY KEY,
#                         nome VARCHAR(100) NOT NULL,
#                         nota1 FLOAT NOT NULL,
#                         nota2 FLOAT NOT NULL,
#                         nota3 FLOAT NOT NULL,
#                         media FLOAT NOT NULL,
#                         situacao VARCHAR(100) NOT NULL)''')
#         self.conexao.commit()

#     def executar_comando(self, comando, valores=None):
#         self.cursor.execute(comando, valores)
#         self.conexao.commit()

#     def buscar_dados(self, comando):
#         self.cursor.execute(comando)
#         return self.cursor.fetchall()

# class Aluno:
#     def __init__(self, nome, nota1, nota2, nota3):
#         self.nome = nome
#         self.nota1 = nota1
#         self.nota2 = nota2
#         self.nota3 = nota3
#         self.media, self.situacao = self.calcular_media()

#     def calcular_media(self):
#         media = (self.nota1 + self.nota2 + self.nota3) / 3
#         situacao = "Aprovado" if media >= 6 else "Reprovado"
#         return media, situacao

# class GerenciadorAlunos:
#     def __init__(self):
#         self.bd = Banco()

#     def validar_notas(self):
#         notas = []
#         for i in range(1, 4):
#             while True:
#                 try:
#                     nota = float(input(f"Digite a nota {i} de 0 a 10: "))
#                     if 0 <= nota <= 10:
#                         notas.append(nota)
#                         break
#                     else:
#                         print("Nota inválida. Digite um valor entre 0 e 10.")
#                 except ValueError:
#                     print("ERRO. Digite um número válido de 0 a 10.")
#         return notas

#     def cadastrar_aluno(self):
#         nome = input("Nome do aluno: ")
#         notas = self.validar_notas()
#         aluno = Aluno(nome, notas[0], notas[1], notas[2])
#         self.bd.executar_comando(
#             '''INSERT INTO aluno (nome, nota1, nota2, nota3, media, situacao) VALUES (%s, %s, %s, %s, %s, %s)''',
#             (aluno.nome, aluno.nota1, aluno.nota2, aluno.nota3, aluno.media, aluno.situacao)
#         )
#         print("Aluno cadastrado.")

#     def exibir_alunos(self):
#         alunos = self.bd.buscar_dados("SELECT * FROM aluno")
#         for i in alunos:
#             print(f"""
#                     ID: {i[0]}
#                     Nome: {i[1]}
#                     Nota1: {i[2]}
#                     Nota2: {i[3]}
#                     Nota3: {i[4]}
#                     Média: {i[5]:.2f}
#                     Situação: {i[6]}
#                     """)

# cadastro = GerenciadorAlunos()
# while True:
#     print("""
#             1 - Cadastrar aluno
#             2 - Exibir alunos
#             3 - Sair
#             """)
#     op = input("Opção: ")
#     if op == "1":
#         cadastro.cadastrar_aluno()
#     elif op == "2":
#         cadastro.exibir_alunos()
#     elif op == "3":
#         break
#     else:
#         print("Opção inválida.")
        
        
# sistema base o curso:
class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo
    def __str__(self): # so para retornar em texto
        return f"Curso: {self.nome} - Período: {self.periodo}"
    
class Pessoa: # classe pai para aluno e profesor
    def __init__(self, nome, data_nasc, matricula):
        self.nome = nome
        self.data_nasc = data_nasc
        self.matricula = matricula
class Professor(Pessoa): # clse filho - professor e alunos
    def __init__(self, nome, disciplina, matricula): # profesor n precisa da data_nasc
        super().__init__(nome, None, matricula)
        # disciplina:
        self.disciplina = disciplina
        
    # str para nome, disciplina e matricula:
    def __str__(self):
        return f""" Professor(a): {self.nome}
                    Disciplina {self.disciplina}
                    Matricula: {self.matricula}"""
                    
class Aluno(Pessoa):
    def __init__(self, nome, data_nasc, matricula):
        super().__init__(nome, data_nasc, matricula)
    def __str__(self):
        return f""" Aluno(a): {self.nome}
                    Idade: {self.data_nasc}
                    Matricula: {self.matricula}"""
                    
# class do sistema que gerencia:
class Sistema_Escolar:
    def __init__(self):
        # llistas para alunos, professores e cursos
        self.alunos = []
        self.profesores = []
        self.cursos = []
    # metodos do sistema: listar, excluir, incluir e pesquisar
    # metodos listar:
    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado no sistema  :(")
        for i , aluno in enumerate (self.alunos):
            print (f"{i} - {aluno} ")
    
    # metodo de incluir aluno:
    def incluir_aluno(self):
        nome = input("Nome do aluno: ")
        nascimentos = input("Data de Nascimento: ")
        matricula = input("Matricula do aluno: ")
        
        # instancia o objeto aluno e passar atributos:
        aluno = Aluno (nome, nascimentos, matricula)
        self.Alunos.append(aluno)
        print(f"Aluno {nome} adicionado com sucesso!")
    
    # excluir aluno:
    def excluir_aluno(self):
        self.listar_alunos()
        if self.alunos:
            indice = int(input("Digite o número do representante a ser excluido: "))
            # if para verificar se esye dentro do indice:
            if 0 <= indice < len(self.alunos):
                aluno_excluido = self.alunos.pop(indice)
                print(f"Aluno exluido {aluno_excluido}")
            else:
                print ("Nùmero invalido!")
    
    # pesquisar aluno:
    def pesquisar_aluno(self):
        nome_aluno = input("Escreva o nome do aluno que deseja pesquisar: ").lower
        # armazemar em uma lista todoos os nomes para comparar:
        encontrados = [
            a for a in self.alunos if nome_aluno in a.nome.lower # encontrar o aluno pelo nome
        ]
        if encontrados:
            for i in encontrados:
                print(i)
        else:
            print("Aluno não encontrado! Verifique a lista de alunos")

# VERSÃO PROFESSOR:
    # metodos listar:
    def listar_professores(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado no sistema  :(")
        for i , professor in enumerate (self.profesores):
            print (f"{i} - {professor} ")
    
    # metodo de incluir aluno:
    def incluir_professores(self):
        nome = input("Nome do professor: ")
        disciplina = input("Disciplina: ")
        matricula = input("Matricula do aluno: ")
        
        # instancia o objeto aluno e passar atributos:
        professor = Professor (nome, disciplina, matricula)
        self.Alunos.append(professor)
        print(f"Professor {nome} adicionado com sucesso!")
    
    # excluir aluno:
    def excluir_profesor(self):
        self.listar_professores()
        if self.alunos:
            indice = int(input("Digite o número do representante a ser excluido: "))
            # if para verificar se esta dentro do indice:
            if 0 <= indice < len(self.profesores):
                professor_excluido = self.profesores.pop(indice)
                print(f"Professor exluido {professor_excluido} com sucesso!")
            else:
                print ("Nùmero invalido!")
    
    # pesquisar aluno:
    def pesquisar_professor(self):
        nome_professor = input("Escreva o nome do professor que deseja pesquisar: ").lower
        # armazemar em uma lista todoos os nomes para comparar:
        encontrados = [
            a for a in self.profesores if nome_professor in a.nome.lower # encontrar o aluno pelo nome
        ]
        if encontrados:
            for i in encontrados:
                print(i)
        else: 
            print("Erro")         
            
# VERSÃO CURSO:
        # metodos listar:
    def listar_cursos(self):
        if not self.cursos:
            print("Curso não encontrado")
        for i , curso in enumerate (self.profesores):
            print (f"{i} - {curso} ")
    
    # metodo de incluir aluno:
    def incluir_curso(self):
        nome = input("Nome do curso: ")
        periodo = input("Periodo do curso: ")
        
        # instancia o objeto aluno e passar atributos:
        curso = Curso (nome)
        self.Curso.append(curso)
        print(f"Curso {nome} adicionado com sucesso!")
    
    # excluir aluno:
    def excluir_curso(self):
        self.listar_cursos()
        if self.alunos:
            indice = int(input("Digite o número do curso a ser excluido: "))
            # if para verificar se esta dentro do indice:
            if 0 <= indice < len(self.cursos):
                curso_excluido = self.cursos.pop(indice)
                print(f"Curso exluido {curso_excluido} com sucesso!")
            else:
                print ("Nùmero invalido!")
    
    # pesquisar aluno:
    def pesquisar_curso(self):
        nome_curso = input("Escreva o nome do curso que deseja pesquisar: ").lower
        # armazemar em uma lista todoos os nomes para comparar:
        encontrados = [
            a for a in self.cursos if nome_curso in a.nome.lower # encontrar o aluno pelo nome
        ]
        if encontrados:
            for i in encontrados:
                print(i)
        else: 
            print("Erro")
    
# menu    
while True:
    escolha = print(""" MENU DE OPÇÕES - SISTEMA ESCOLAR
          0 - Sair
          -- ALUNOS --
          1 - Ver lista de alunos
          2 - Cadastrar novo aluno
          3 - Excluir aluno
          4 - Pesquisar aluno 
          -- PROFESSORES --
          5 - Ver lista de professores
          6 - Cadastrar novo professor
          7 - Excluir professor
          8 - Pesquisar professor 
          -- CURSOS --
          9 - Ver lista de cursos
          10 - Cadastrar novo curso
          11 - Excluir curso  
          """)
    if escolha == 0:
        print("Saindo do sistema...")
        break
    elif escolha == 1:
        
             
            
            
            
            
            
            
            
            
            

# sistema = Sistema_Escolar()
# sistema.incluir_aluno()
# sistema.listar_alunos()
# sistema.pesquisar_aluno()
# sistema.excluir_aluno()
# sistema.listar_alunos()