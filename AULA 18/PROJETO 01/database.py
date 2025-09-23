#dabase.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

# import sqlite3
# criar a conexão com o banco Sqlite
# o arquivo do banco de dados criar local
DATABASE_URL = "sqlite:///./meubanco.db"

# engine do banco
engine = create_engine(DATABASE_URL, connect_args={
    "check_same_thread":False
})

# criar a sessão do banco de dados usado para consultas de usuário
SessionLocal = sessionmaker(bind=engine)

# classe base para os models
Base = declarative_base()