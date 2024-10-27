from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.orm import declarative_base, sessionmaker
from dataclasses import dataclass
from Funcoes import criando

BD = create_engine("sqlite:///notasbd.bd")

Base = declarative_base()

Session = sessionmaker(bind=BD)
session = Session()

@dataclass
class Diario(Base):
    __tablename__ = "darios"
    id = Column(Integer, primary_key=True,autoincrement=True)
    data = Column(String)
    titulo = Column(String)
    texto = Column(String)

Base.metadata.create_all(bind=BD) 

while True:
    criando()

