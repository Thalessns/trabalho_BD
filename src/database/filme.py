from database.db import connect;
from utils import get_input;

class Filme:

    def __init__(self):
        self.conn = connect();
        self.cursor = self.conn.cursor();

    
    def preparar_insercao(self):
        self.cursor.execute("""SHOW COLUMNS FROM Filmes""")
        campos = self.cursor.fetchall()
        data = {}
        for value in campos:
            data[value[0]] = get_input(f"Informe o {value[0]} que é do tipo {value[1]}: ");
        self.inserir(data)


    def inserir(self, data: dict):        
        query_data = (
            data["IdFilme"],
            data["TituloOriginal"],
            data["TituloNoBrasil"],
            data["AnoProducao"],
            data["LocaisEstreia"],
            data["DataEstreia"],
            data["ArrecadacaoPrimAno"],
            data["Classe"]
        );
        query = """INSERT INTO Filmes (IdFilme, TituloOriginal, TituloNoBrasil, AnoProducao, LocaisEstreia, DataEstreia, ArrecadacaoPrimAno, Classe) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""";

        self.cursor.execute(query, query_data);
        self.conn.commit();

    def select_all(self):
        self.cursor.execute("""SELECT * FROM Filmes""")
        return self.cursor.fetchall();