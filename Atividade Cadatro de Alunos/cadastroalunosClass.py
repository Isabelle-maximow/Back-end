from bancoClass import Banco
from alunoClass import Aluno

class CadastroAluno:
    def __init__(self):
        self.alunos_ = []  
        self.banco = Banco()

    def cadastrar_aluno(self):
        self.conexao, self.cursor = self.conectar_db 
        while True:
            nome = input("Nome do aluno: ")
            aluno = Aluno(nome)
            aluno.add_notas()
            aluno.calculo_media()
            self.alunos_.append(aluno)
            self.cursor.execute('''INSERT INTO alunos
                (nome, nota1, nota2, nota3, media, situacao) VALUES (?,?,?,?,?,?)''',
                (aluno.nome, aluno.notas[0], aluno.notas[1], aluno.notas[2], aluno.media, aluno.situacao))
            
            continuar = input("Digite 's' para sair ou Enter para continuar: ").lower()
            if continuar == "s":
                print("Saindo do sistema...")
                break
            self.cursor.execute('''INSERT INTO alunos
                (nome, nota1, nota2, nota3, media, situacao) VALUES (?,?,?,?,?,?)''',
                (nome, self.notas[0], self.notas[1], self.notas[2], self.media, self.situacao))
            
        self.conexao.commit()
        self.conexao.close()

    def exibir_alunos(self):
        for aluno in self.alunos_:
            aluno.exibir_dados()