'''
ISABELLE FERREIRA
24271526
'''
import sqlite3

class BancoDeDados:
    def __init__(self,nome_db="escola.db"):
        self.nome_db=nome_db
        self.conexao=sqlite3.connect(nome_db)        
        self.cursor=self.conexao.cursor()
        self.criar_tabela_aluno()
        self.criar_tabela_professor()
        self.criar_tabela_curso()
        
    # tabela Aluno
    def criar_tabela_aluno(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            matricula TEXT NOT NULL)''')
        self.conexao.commit()
        
    # tabela Professor
    def criar_tabela_professor(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS professores (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            disciplina TEXT NOT NULL,
                            matricula TEXT NOT NULL)''')
        self.conexao.commit()  
        
    # tabela Cursos
    def criar_tabela_curso(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cursos (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            periodo TEXT NOT NULL)''')
        self.conexao.commit()  
    def fechar_conexao(self):
        self.conexao.close()
    def executar_comando(self,comando,parametro=()):
        self.cursor.execute(comando,parametro)
        self.conexao.commit()
    def buscar_dados(self,comando,parametro=()):
        self.cursor.execute(comando,parametro)
        return self.cursor.fetchall()
    

class Curso:
    def __init__(self,nome,periodo):
        self.nome=nome
        self.periodo=periodo
    
    def __str__(self):
        return f"Curso: {self.nome} - Perido: {self.periodo}."
    
class Pessoa:
    def __init__(self,nome,data_nasc,matricula):
        self.nome=nome
        self.data_nasc=data_nasc
        self.matricula=matricula
        
class Professor(Pessoa):
    def __init__(self, nome, disciplina, matricula):
        super().__init__(nome, None, matricula)
        self.disciplina=disciplina
        self.matricula=matricula
        # professor não precisa de data de nascimento apenas disciplin
        
    #passar uma string nome e disciplina
    def __str__(self):
        return f"""Professor(a): {self.nome}    
        Disciplina: {self.disciplina}
        Matricula: {self.matricula}"""
        
class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome, None, matricula)
        
    
    def __str__(self):
        return f"""Aluno: {self.nome}
        Matricula: {self.matricula}"""
        
#classe principal que gerencia o sistema
class SistemaEscolar:
    def __init__(self):
        self.db=BancoDeDados()
        
# ALUNOS 
    #metodo aluno
    def listar_aluno(self):
        alunos = self.db.buscar_dados("SELECT * FROM alunos")
        if not alunos:
            print("Nenhum aluno fou encontrado.")
        for i in alunos:
            print(f"""
                    ID: {i[0]}
                    Nome: {i[1]}
                    Matricula: {i[2]}""")         
             
    #metodo incluir aluno
    def incluir_aluno(self):
        nome= input("Digite o nome do aluno: ").lower()
        matricula=input("Digite a matricula do aluno: ")
        aluno  = Aluno(nome,matricula)
        self.db.executar_comando('''INSERT INTO alunos (
        nome,matricul) VALUES (?,?,?)''',
        (aluno.nome, aluno.matricula))
        print(f"Aluno {nome} adicionado!")
        
    #metodo excluir aluno
    def excluir_aluno(self):
        self.listar_aluno()
        id_aluno = int(input("Digite o id do aluno a ser excluido: "))
        self.db.executar_comando("DELETE FROM alunos WHERE id=?", (id_aluno,))
        print(f"Aluno com {id_aluno} deletado com sucesso. ")
        
    #metodo pesquisar aluno
    def pesquisar_aluno(self):
        nome_aluno = input("Digite o nome do aluno para pesquisar: ").lower()
        aluno = self.db.buscar_dados("SELECT * FROM  alunos WHERE nome=?", (nome_aluno,))
        if not aluno:
            print(f"Aluno {nome_aluno} não encontado.")
        else:
            for i in aluno:
                print(f"""
                        ID: {i[0]}
                        Nome: {i[1]}
                        Matricula: {i[2]}""")

# PROFESSORES 
    #metodo professor
    def listar_professor(self):
        professores = self.db.buscar_dados("SELECT * FROM professores")
        if not professores:
            print("Nenhum professor encontrado")
        for i in professores:
            print(f"""
                    ID: {i[0]}
                    Nome: {i[1]}
                    Disciplina: {i[2]}
                    Matricula: {i[3]}                
                    """)  
            
    #metodo incluir professor
    def incluir_professor(self):
        nome= input("Digite o nome do professor: ")
        disciplina=input("Digite a disciplina do professor: ")
        matricula=input("Digite a matricula do professor: ")
        professor  = Professor(nome,disciplina,matricula)
        self.db.executar_comando('''INSERT INTO professores (
        nome,disciplina,matricula) VALUES (?,?,?)''',
        (professor.nome,professor.disciplina,professor.matricula))
        print(f"Professor {nome} adicionado!")  
        
    # excluir professor
    def excluir_professor(self):
        self.listar_professor()
        id_professor = int(input("Digite o id do professor a ser exlcuido: "))
        self.db.executar_comando("DELETE FROM professores WHERE id=?", (id_professor,))
        print(f"Professor com {id_professor} deletado com sucesso.")
        
    #metodo pesquisar professor
    def pesquisar_professor(self):
        nome_professor = input("nome do professor: ").lower()
        professor=self.db.buscar_dados("SELECT * FROM professores WHERE nome=?", (nome_professor)) 
        if not professor:
            print(f"Professor {nome_professor} não encontado.")
        else:
            for i in professor:
                print(f"""
                        ID: {i[0]}
                        Nome: {i[1]}
                        Matricula: {i[2]}""")
# CURSOS 
    # cursos
    def lista_cursos(self):
        cursos = self.db.buscar_dados("SELECT * FROM cursos")
        if not cursos:
            print("Nenhum curso foi encontrado.")
        for i in cursos:
            print(f"""
                    ID: {i[0]}
                    nome: {i[1]}
                    periodo: {i[2]}                
                    """) 
        
    # incluir curso
    def incluir_curso(self):
        nome = input("Digite o nome do curso: ")
        periodo = input("Digite o periodo do curso: ")
        curso =  Curso(nome,periodo)
        self.db.executar_comando('''INSERT INTO cursos (
        nome,periodo) VALUES (?,?)''',
        (curso.nome,curso.periodo))
        print(f"Curso {nome} cadastrado.")
        
    # excluir curso
    def excluir_curso(self):
        self.lista_cursos()
        id_curso = int(input("Digite o id do curso a ser exlcuido: "))
        self.db.executar_comando("DELETE FROM cursos WHERE id=?", (id_curso,))
        print(f"Curso {id_curso} deletado com sucesso.")
        
    # pesquidar curso
    def pesquisar_curso(self):
        nome_curso = input("nome do curso para pesquisar: ").lower()
        curso=self.db.buscar_dados("SELECT * FROM cursos WHERE nome=?", (nome_curso))   
        if not curso:
            print(f"Curso {nome_curso} não encontado.")
        else:
            for i in curso:
                print(f"""
                        ID: {i[0]}
                        Nome: {i[1]}
                        Periodo: {i[2]}""")
def main():
    sistema = SistemaEscolar()
    while True:
        print("""
    MENU:
        0 - Sair
        1 - Ver lista de alunos
        2 - Incluir novo aluno
        3 - Excluir aluno
        4 - Pesquisar aluno

        5 - Ver lista de professores
        6 - Incluir novo professor
        7 - Excluir professor
        8 - Pesquisar professor

        9 - Ver lista de cursos
        10 - Incluir novo curso
        11 - Excluir curso
        12 - Pesquisar curso
              """)
        escolha = input("Digite a escolha: ")

        if escolha == "1":
            sistema.listar_aluno()
        elif escolha == "2":
            sistema.incluir_aluno()
        elif escolha == "3":
            sistema.excluir_aluno()
        elif escolha == "4":
            sistema.pesquisar_aluno()

        elif escolha == "5":
            sistema.listar_professor()
        elif escolha == "6":
            sistema.incluir_professor()
        elif escolha == "7":
            sistema.excluir_professor()
        elif escolha == "8":
            sistema.pesquisar_professor()
        elif escolha == "9":
            sistema.lista_cursos()
        elif escolha == "10":
            sistema.incluir_curso()
        elif escolha == "11":
            sistema.excluir_curso()
        elif escolha == "12":
            sistema.pesquisar_curso()

        elif escolha == "0":
            print("Saindo do sistema...")
            break
        else:print(f"ERRO {escolha} não encontrada.") 
main()
    