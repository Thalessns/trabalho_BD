from db import connect;

class Enominado:
    def __init__(self):
        self.con = connect();
        self.cursor = self.con.cursor();

    def inserir (self, data: dict):

        query_data = (data['Premio'], data['Filme'], data['Pessoa'], data['Ganhou']);

        query = """INSERT INTO ENominado(Premio, Filme, Pessoa, Ganhou)
                    Values(%s, %s, %s, %s)""";

        self.cursor.execute(query, query_data);
        self.con.commit();
