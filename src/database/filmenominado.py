from database.db import connect;
from utils import get_input;

class FilmeNominado:
    def __init__(self):
        self.con = connect()
        self.cursor = self.con.cursor()
    

    def preparar_insercao(self):
        self.cursor.execute("""SHOW COLUMNS FROM Filmenominado""")
        campos = self.cursor.fetchall()
        data = {}
        for value in campos:
            data[value[0]] = get_input(f"Informe o {value[0]} que é do tipo {value[1]}: ");
        self.inserir(data)


    def inserir(self, data : dict):
        
        query_data = (data['Premio'], data['Filme'], data['Premiado'])

        query = """
            INSERT INTO FilmeNominado (Premio, Filme, Premiado)
            VALUES (%s, %s, %s)
        """

        self.cursor.execute(query, query_data)
        self.con.commit()

    def select_premio (self, codpremio: int):
        query = f"""
             SELECT TituloOriginal, TituloNoBrasil, Premiado FROM Filmenominado AS fn, Filmes as f WHERE fn.Premio = {codpremio} AND fn.Filme = f.idFilme;
            """
        self.cursor.execute(query);
        return self.cursor.fetchall();

    def select_all(self):
        self.cursor.execute("""SELECT * FROM Filmenominado""")
        return self.cursor.fetchall();

