from database.db import connect;
from utils import get_input;


class Evento:
    def __init__ (self):
        self.con = connect();
        self.cursor = self.con.cursor();

    def preparar_insercao(self):
        self.cursor.execute("""SHOW COLUMNS FROM Eventos""")
        campos = self.cursor.fetchall()
        data = {}
        for value in campos:
            data[value[0]] = get_input(f"Informe o {value[0]} que é do tipo {value[1]}: ");
        self.inserir(data=data)


    def inserir(self, data:dict):

        query_data = (data['Nome'], data['Ano'], data['Nacionalidade'], data['Tipo'], data['AnoInicio']);

        query = """INSERT INTO Eventos(Nome, Ano, Nacionalidade, Tipo, AnoInicio)
                    VALUES(%s, %s, %s, %s, %s)""";

        self.cursor.execute(query, query_data);
        self.con.commit();
