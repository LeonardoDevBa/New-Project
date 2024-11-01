from datetime import datetime
from sqlalchemy import create_engine, String, Column,DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from dataclasses import dataclass
from Funcoes import criando,menu,excluir_anotacao
import os
from time import sleep
os.system("cls||clear")


BD = create_engine("sqlite:///notasbd.bd")

Base = declarative_base()

Session = sessionmaker(bind=BD)
session = Session()

@dataclass
class Diario(Base):
    __tablename__ = "darios"
    data = Column(DateTime,primary_key=True)
    titulo = Column(String)
    texto = Column(String)

Base.metadata.create_all(bind=BD) 

while True:
    sleep(5)
    os.system("cls||clear")
    menu()
    opcao =int(input(": "))
    if opcao in [1, 2, 3, 4]:
        match opcao:
            case 1:
                dia_pesquisa = int(input("DIA: "))
                mes_pesquisa = int(input("MÊS: "))
                ano_pesquisa = int(input("ANO: "))
                data_pesquisa = datetime(ano_pesquisa, mes_pesquisa, dia_pesquisa)
                anotacao = session.query(Diario).filter(Diario.data == data_pesquisa).first()
                print("="*20)
                if anotacao:
                    print(f"{anotacao.titulo:^20}")
                    print("="*20)
                    print(anotacao.texto)
                else:
                    print("Nenhuma anotação encontrada para essa data.")
            case 2:
                criando()
            case 3:
                excluir_anotacao()
            case 4:
                anotacao = session.query(Diario).all()
                print("="*20)
                if anotacao:
                    for item in anotacao:
                        print("="*20)
                        print(f"{item.titulo:^20}")
                        print("="*20)
                        print(f"Data/Horas: {item.data}")
                        print(item.texto)


    else:            
        print("OPÇÂO INVALIDA")





