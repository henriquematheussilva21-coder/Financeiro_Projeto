from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "financeiro.db")

class Base(DeclarativeBase):
    pass

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)
Session = sessionmaker(bind=engine)

def get_session():
    """Retorna uma nova sessão do banco."""
    return Session()

def criar_tabelas():
    """Cria as tabelas no banco se não existirem."""
    Base.metadata.create_all(engine)