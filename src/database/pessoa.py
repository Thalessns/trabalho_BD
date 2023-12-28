from db import connect;

class Pessoa:

    def __init__(self):
        self.connection = connect();
        self.cursor = self.connection.cursor();

    def inserir(self, data: dict):
        
        query_data = (
            data["NomeArt"],
            data["NomeVerd"],
            data["Sexo"],
            data["AnoNasc"],
            data["Site"],
            data["AnoInic"],
            data["Situacao"],
            data["NroTotalAnos"]
        );

        query = """ INSERT INTO pessoa (NomeArt, NomeVerd, Sexo, AnoNasc, Site, AnoInic, Situacao, NroTotalAnos) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) """;

        self.cursor.execute(query, query_data);
        self.connection.commit();

