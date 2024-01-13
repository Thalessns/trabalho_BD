from database.db import connect;

class LocalEstreia:

    def __init__(self):
        self.conn   = connect();
        self.cursor = self.conn.cursor();

    def inserir(self, data: dict):        
        query_data = (
            data["IdLocal"],
            data["Cinema"],
            data["Sala"]
        );
        query = """INSERT INTO LocalEstreia (IdLocal, Cinema, Sala) VALUES (%s, %s, %s)""";

        self.cursor.execute(query, query_data);
        self.conn.commit();

inst = LocalEstreia();
inst.inserir({"IdLocal": "", "Cinema": "Cinema de Franco da Rocha", "Sala": 3});