from db import connect;

class Filme:

    def __init__(self):
        self.conn = connect();
        self.cursor = self.conn.cursor();


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

        self.cursor.execute(query, tupla);
        self.conn.commit();