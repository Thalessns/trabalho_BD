from database.db import connect;
from utils import get_input;

class Premio:
    def __init__(self):
        self.con = connect()
        self.cursor = self.con.cursor()


    def preparar_insercao(self):
        self.cursor.execute("""SHOW COLUMNS FROM Premio""")
        campos = self.cursor.fetchall()
        data = {}
        for value in campos:
            if value[0] == "CodPremio": continue;
            data[value[0]] = get_input(f"Informe o {value[0]} que é do tipo {value[1]}: ");
        self.inserir(data)


    def inserir(self, data:dict):

        query_data = (data['Tipo'], data['Nome'])

        query = """ INSERT INTO Premio(Tipo, Nome) 
                    VALUES (%s, %s) """

        self.cursor.execute(query, query_data)
        self.con.commit()

    def select_tipo(self, cod_premio: int):
        self.cursor.execute(f"""SELECT Tipo FROM Premio WHERE CodPremio = {cod_premio}""");
        r = self.cursor.fetchone();
        if r is None: return
        return r[0]

    def select_all(self):
        self.cursor.execute("""SELECT * FROM Premio""")
        return self.cursor.fetchall();
