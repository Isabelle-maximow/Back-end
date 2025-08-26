import mysql.connector

CONFIG_BANCO = {
    'host': 'localhost', # local do servidor de banco
    'user': 'root', # usuario que vi logar no servidor
    'password': 'dev1t@24', # senha definida no servidor 
    'database': 'BANCO 02', # nome do banco de dados
}
conexao = mysql.connector.connect(**CONFIG_BANCO) # conectando
cursor = conexao.cursor()

# BANCO_DE_DADOS = "aluno.db"
class Banco:
    def __init__(self, **CONFIG_BANCO):
        self.conexao = mysql.connector.connect(**CONFIG_BANCO) # conectando
        self.cursor = conexao.cursor()
        # self.conectar_db()
        
    def conectar_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS aluno (
                        nome VARCHAR (100) NOT NULL,
                        nota1 FLOAT NOT NULL,
                        nota2 FLOAT NOT NULL,
                        nota3 FLOAT NOT NULL,
                        media INT NOT NULL,
                        situacao VARCHAR (100) NOT NULL)''')  # Criação
        self.conexao.commit()

class Aluno:
    def __init__(self, nome):
        self.notas = []
        self.nome = nome
        self.media = 0.0  # média
        self.situacao = ""  # aprovado ou reprovado

    def add_notas(self):
        for i in range(1,4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i}: "))
                    if 0 <= nota <= 10:
                        self.notas.append(nota)
                        break
                    else:
                        print("Valor inexistente. Digite uma nota entre 0 e 10.")
                except ValueError:
                    print("Erro: digite um número válido.")

    def calculo_media(self):
        if self.notas:
            self.media = sum(self.notas) / len(self.notas)
            self.situacao = "Aprovado" if self.media >= 6 else "Reprovado"
        else:
            self.media = 0.0
            self.situacao = "Sem notas"

    def exibir_dados(self):
        print(f"""
            Nome: {self.nome}
            Notas: {self.notas}
            Média: {self.media:.2f}
            Situação: {self.situacao}
        """)

class CadastroAluno:
    def __init__(self):
        self.alunos_ = []  
        self.banco = Banco()

    def cadastrar_aluno(self):
        self.conexao, self.cursor = self.banco.conexao, self.banco.cursor
        while True:
            nome = input("Nome do aluno: ")
            aluno = Aluno(nome)
            aluno.add_notas()
            aluno.calculo_media()
            self.alunos_.append(aluno)
            self.cursor.execute('''INSERT INTO aluno
                (nome, nota1, nota2, nota3, media, situacao) VALUES (?,?,?,?,?,?)''',
                (aluno.nome, aluno.notas[0], aluno.notas[1], aluno.notas[2], aluno.media, aluno.situacao))  # Inserção
            
            continuar = input("Digite 's' para sair ou Enter para continuar: ").lower()
            if continuar == "s":
                print("Saindo do sistema...")
                break
            self.cursor.execute('''INSERT INTO aluno
                (nome, nota1, nota2, nota3, media, situacao) VALUES (?,?,?,?,?,?)''',
                (nome, self.notas[0], self.notas[1], self.notas[2], self.media, self.situacao))
            
        self.conexao.commit()
        self.conexao.close()

    def exibir_alunos(self):
        for aluno in self.alunos_:
            aluno.exibir_dados()

def main():
    print("Cadastro de alunos...")
    sistema = CadastroAluno()
    sistema.cadastrar_aluno()
    sistema.exibir_alunos()

if __name__ == "__main__":
    main()
    

'''
Exercicio:
MUDAR P MARIADB
'''
