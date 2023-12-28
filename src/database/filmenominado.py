from db import connect;

class FilmeNominado:
    def __init__(self):
        self.con = connect()
        self.cursor = self.con.cursor()
    
    def inserir(self, data : dict):
        
        query_data = (data['Premio'], data['Filme'], data['Premiado'])

        query = """
            INSERT INTO FilmeNominado (Premio, Filme, Premiado)
            VALUES (%s, %s, %s)
        """

        self.cursor.execute(query, query_data)
        self.con.commit()
