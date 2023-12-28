from db import connect;

class Evento:
    def __init__ (self):
        self.con = connect();
        self.cursor = self.con.cursor();

    def inserir(self, data:dict):

        query_data = (data['Nome'], data['Ano'], data['Nacionalidade'], data['Tipo'], data['AnoInicio']);

        query = """INSERT INTO Eventos(Nome, Ano, Nacionalidade, Tipo, AnoInicio)
                    VALUES(%s, %s, %s, %s, %s)""";

        self.cursor.execute(query, query_data);
        self.con.commit();
