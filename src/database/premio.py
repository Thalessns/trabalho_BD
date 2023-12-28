from db import connect;

class Premio:
    def __init__(self):
        self.con = connect()
        self.cursor = self.con.cursor()

    def inserir(self, data:dict):

        query_data = (data['Tipo'], data['Nome'])

        query = """ INSERT INTO Premio(Tipo, Nome) 
                    VALUES (%s, %s) """

        self.cursor.execute(query, query_data)
        self.con.commit()