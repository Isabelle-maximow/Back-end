#converter o sistema alunos para orm
#padrão imports 
from sqlalchemy import create_engine,Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#conexão com o mariadb
#mudae a senha do root com do mariadb
#senha sem @
#pip install mysql-connector
##pip install pymysql
#dev_a
#dev1t#24

engine=create_engine('mysql+pymysql://dev_a:dev1t#24@localhost:3306/alunos_orm' ,echo=True)
Base=declarative_base()
class Aluno(Base):
    __tablename__ = 'Alunos'
    id = Column(Integer,primary_key=True,autoincrement=True)
    nome = Column(String(255), nullable=False)
    nota1 = Column(Float, nullable=False)
    nota2 = Column(Float, nullable=False)
    media = Column(Float, nullable=False)
    situacao = Column(String(100), nullable=False)
    #retorna os dados em formato de str pro sistema 
    def __repr__(self):
        return f'''Dados dos alunos:
        Nome: {self.nome}    Nota 1: {self.nota1}  Nota 2: {self.nota2}
        Média: {self.media}  Situação: {self.situacao}'''
#criar a tabela 
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

#OPCIONAL
def validar_nome():
    pass
def validar_notas():
    pass
def media():
    pass
def cadastrar_aluno():
    session = Session()
    try:
        nome = input('Nome do aluno:')
        nota1 = float(input('Nota 1:'))
        nota2 = float(input('Nota 2:'))
        nota2 = float(input('Nota 2:'))
        media  =float(input('Media: '))
        situacao = input('Situação: ')
        novo_aluno=Aluno(nome=nome,nota1=nota1,nota2=nota2,media=media, situacao=situacao)
        session.add(novo_aluno)
        session.commit()
        print('Aluno Cadastrado! ')
    except Exception as erro: 
        print(f'ERRO: {erro}')
        session.rollback()#desfazer alterações em caso de erro
    finally:session.close()
#cadastrar_aluno()
def exibir_aluno():
    session=Session()
    try:
        alunos=session.query(Aluno).all()
        for i in alunos:
            print(f"ID:{i.id} Nome:{i.nome}")
    except Exception as erro:
        print(f"ERRO:{erro}")
    finally:session.close()
#exibir_aluno()
def atualizar():
    exibir_aluno()
    session=Session()
    try:
        id_aluno=int(input("ID para atualizar"))
        aluno=session.query(Aluno).filter(Aluno.id==id_aluno).first()
        if aluno:
            #novos dados para atualizar
            nota1=float(input("Nova nota-1 do aluno:"))
            nota2=float(input("Nova nota-2 do aluno:"))
            #atualizar
            aluno.nota1=nota1
            aluno.nota2=nota2
            session.commit()
        else:print("ID não encontrado:")
    except Exception as erro:
        print(f"ERRO:{erro}")
        session.rollback()
    finally:session.close()
#atualizar()
def deletar():
    exibir_aluno()
    session=Session()
    try:
        id_aluno=int(input("ID para deletar"))
        aluno=session.query(Aluno).filter(Aluno.id==id_aluno).first()
        if aluno:
            session.delete(aluno)
            session.commit()
        else:print("ID não encontrado:")
    except Exception as erro:
        print(f"ERRO:{erro}")
        session.rollback()
    finally:session.close()
#deletar()
def menu():
    while True:
        print("""Opções:
            1-Inserir Aluno:
            2-Visualizar Aluno:
            3-Atualizar Aluno:
            4-Deletar Aluno:
            0- Sair:""")
        op=input("Escolha:")
        if op=="1":cadastrar_aluno()
        elif op=="2":exibir_aluno()
        elif op =="3":atualizar()
        elif op =="4":deletar()
        elif op =="0":break
        else:print("opção inválida:")
if __name__ =="__main__":
    menu()