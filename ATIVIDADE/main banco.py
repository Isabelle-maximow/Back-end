
import mysql.connector

CONFIG_BANCO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'dev1t@24',
    'database': 'sistemaescolar'
}

class Bancodedados:
    def __init__(self, nome=CONFIG_BANCO):
        self.nome = nome
        self.conexao = mysql.connector.connect(**nome)
        self.cursor = self.conexao.cursor()
        self.criar_tabela_alunos()
        self.criar_tabela_professor()
        self.criar_tabela_curso()

    def criar_tabela_alunos(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome VARCHAR(100) NOT NULL,
                            data_nasc VARCHAR(10) NOT NULL,
                            matricula INT NOT NULL)
                                                ''')
        self.conexao.commit()

    def criar_tabela_professor(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS professor (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome VARCHAR(100) NOT NULL,
                            disciplina VARCHAR(100) NOT NULL,
                            matricula INT NOT NULL)
                                                ''')
        self.conexao.commit()

    def criar_tabela_curso(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS curso (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nome VARCHAR(100) NOT NULL,
                            periodo VARCHAR(10) NOT NULL)
                                                ''')
        self.conexao.commit()

    def executar_comando(self, comando, parametros=()):
        self.cursor.execute(comando, parametros)
        self.conexao.commit()

    def buscar_dados(self, comando):
        self.cursor.execute(comando)
        return self.cursor.fetchall()

    def fechar_conexao(self):
        self.conexao.close()

# CLASSES
class Curso:
    def __init__(self, nome, periodo):
        self.nome = nome
        self.periodo = periodo

    def __str__(self):
        return f"Curso: {self.nome} - Periodo {self.periodo}"

class Pessoa:
    def __init__(self, nome, data_nasc, matricula):
        self.nome = nome
        self.data_nasc = data_nasc
        self.matricula = matricula

class Professor(Pessoa):
    def __init__(self, nome, disciplina, matricula):
        super().__init__(nome, None, matricula)
        self.disciplina = disciplina

    def __str__(self):
        return f"Professor: {self.nome} | Disciplina: {self.disciplina}  | Matrícula: {self.matricula}"

class Aluno(Pessoa):
    def __init__(self, nome, data_nasc, matricula):
        super().__init__(nome, data_nasc, matricula)

    def __str__(self):
        return f"Aluno: {self.nome} | Data de nascimento: {self.data_nasc} | Matrícula: {self.matricula}"

class SistemaEscolar:
    def __init__(self):
        self.alunos = []
        self.professores = []
        self.cursos = []
        self.bd = Bancodedados()

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno encontrado.")
        for i, aluno in enumerate(self.alunos):
            print(f"{i} - {aluno}")

    def incluir_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        data = input("Digite a data de nascimento do aluno: ")
        aluno = Aluno(nome, data, matricula)
        self.alunos.append(aluno)
        print(f"Aluno: {nome} incluído com sucesso!")
        self.bd.executar_comando("INSERT INTO alunos (nome, data_nasc, matricula) VALUES (%s, %s, %s)",
                                 (aluno.nome, aluno.data_nasc, aluno.matricula))

    def excluir_aluno(self):
        self.listar_alunos()
        if self.alunos:
            indice = int(input("Digite o índice do aluno a ser excluído: "))
            if 0 <= indice < len(self.alunos):
                aluno_excluido = self.alunos.pop(indice)
                print(f"Aluno {aluno_excluido.nome} excluído.")
            else:
                print("Índice inválido.")

    def pesquisar_aluno(self):
        termo = input("Digite o nome do aluno para pesquisa: ").upper()
        encontrados = [a for a in self.alunos if termo in a.nome.upper()]
        if encontrados:
            for aluno in encontrados:
                print(aluno)
        else:
            print("Aluno não encontrado.")

    def listar_professores(self):
        if not self.professores:
            print("Nenhum professor encontrado.")
        for i, prof in enumerate(self.professores):
            print(f"{i} - {prof}")

    def incluir_professor(self):
        nome = input("Digite o nome do professor: ")
        disciplina = input("Digite a disciplina: ")
        matricula = input("Digite a matrícula: ")
        professor = Professor(nome, disciplina, matricula)
        self.professores.append(professor)
        print(f"Professor {nome} incluído com sucesso!")
        self.bd.executar_comando("INSERT INTO professor (nome, disciplina, matricula) VALUES (%s, %s, %s)",
                                 (professor.nome, professor.disciplina, professor.matricula))

    def excluir_professor(self):
        self.listar_professores()
        if self.professores:
            indice = int(input("Digite o índice do professor a ser excluído: "))
            if 0 <= indice < len(self.professores):
                prof_excluido = self.professores.pop(indice)
                print(f"Professor {prof_excluido.nome} excluído.")
            else:
                print("Índice inválido.")

    def pesquisar_professor(self):
        termo = input("Digite o nome do professor para pesquisa: ").upper()
        encontrados = [p for p in self.professores if termo in p.nome.upper()]
        if encontrados:
            for prof in encontrados:
                print(prof)
        else:
            print("Professor não encontrado.")

    def listar_cursos(self):
        if not self.cursos:
            print("Nenhum curso cadastrado.")
        for i, curso in enumerate(self.cursos):
            print(f"{i} - {curso}")

    def incluir_curso(self):
        nome = input("Digite o nome do curso: ")
        periodo = input("Digite o período do curso: ")
        curso = Curso(nome, periodo)
        self.cursos.append(curso)
        print(f"Curso {nome} incluído com sucesso!")
        self.bd.executar_comando("INSERT INTO curso (nome, periodo) VALUES (%s, %s)",
                                 (curso.nome, curso.periodo))

    def excluir_curso(self):
        self.listar_cursos()
        if self.cursos:
            indice = int(input("Digite o índice do curso a ser excluído: "))
            if 0 <= indice < len(self.cursos):
                curso_excluido = self.cursos.pop(indice)
                print(f"Curso {curso_excluido.nome} excluído.")
            else:
                print("Índice inválido.")

    def pesquisar_curso(self):
        termo = input("Digite o nome do curso para pesquisa: ").upper()
        encontrados = [c for c in self.cursos if termo in c.nome.upper()]
        if encontrados:
            for curso in encontrados:
                print(curso)
        else:
            print("Curso não encontrado.")

    def executar(self):
        print("Bem-vindo ao Sistema Escolar!")
        while True:
            print("""
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
            opcao = input("Escolha uma opção: ")

            if opcao == "0":
                print("Saindo do sistema...")
                self.bd.fechar_conexao()  
                break
            elif opcao == "1":
                self.listar_alunos()
            elif opcao == "2":
                self.incluir_aluno()
            elif opcao == "3":
                self.excluir_aluno()
            elif opcao == "4":
                self.pesquisar_aluno()
            elif opcao == "5":
                self.listar_professores()
            elif opcao == "6":
                self.incluir_professor()
            elif opcao == "7":
                self.excluir_professor()
            elif opcao == "8":
                self.pesquisar_professor()
            elif opcao == "9":
                self.listar_cursos()
            elif opcao == "10":
                self.incluir_curso()
            elif opcao == "11":
                self.excluir_curso()
            elif opcao == "12":
                self.pesquisar_curso()
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    sistema = SistemaEscolar()
    sistema.executar()
