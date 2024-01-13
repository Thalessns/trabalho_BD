from db import connect;
from utils import get_input;

class Pessoa:

    def __init__(self):
        self.connection = connect();
        self.cursor = self.connection.cursor();
    

    def preparar_insercao(self):
        self.cursor.execute("""SHOW COLUMNS FROM pessoa""")
        campos = self.cursor.fetchall()
        data = {}
        for value in campos:
            data[value[0]] = get_input(f"Informe o {value[0]} que é do tipo {value[1]}: ");
        self.inserir(data)


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

    def select_all(self):
        self.cursor.execute("""SELECT * FROM Pessoa""")
        return self.cursor.fetchall();
