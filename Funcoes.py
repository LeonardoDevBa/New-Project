def criando ():
    from main import Diario, session
    diario = Diario(
        data = input("DATA: "),
        titulo = input("TITULO: "),
        texto = input("")
    )
    session.add(diario)
    session.commit