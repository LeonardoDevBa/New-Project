def menu():
    print("""
1- CHECAR ANOTAÇÕES
2- ADICIONAR ANOTAÇÃO
3- EXCLUIR ANOTAÇÃO
""")
    
def criando ():
    from main import Diario, session,datetime
    dia_pesquisa = int(input("DIA: "))
    mes_pesquisa = int(input("MÊS: "))
    ano_pesquisa = int(input("ANO: "))
    data_time = datetime(ano_pesquisa, mes_pesquisa, dia_pesquisa)
    diario = Diario(
        data=data_time,
        titulo=input("TITULO: "),
        texto=input("TEXTO: ")
    )
    session.add(diario)
    session.commit()
    print("Anotação adicionada com sucesso!")

def excluir_anotacao():
    from main import Diario, session,datetime
    dia_pesquisa = int(input("DIA: "))
    mes_pesquisa = int(input("MÊS: "))
    ano_pesquisa = int(input("ANO: "))
    
    data_time = datetime(ano_pesquisa, mes_pesquisa, dia_pesquisa)
    
    anotacao = session.query(Diario).filter(Diario.data == data_time).first()
    
    if anotacao:
        session.delete(anotacao)
        session.commit()
        print("Anotação excluída com sucesso!")
    else:
        print("Nenhuma anotação encontrada para essa data.")
