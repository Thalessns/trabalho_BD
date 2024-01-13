from db import connect;
from utils import get_input;

class Enominado:
    def __init__(self):
        self.con = connect();
        self.cursor = self.con.cursor();

    def preparar_insercao(self):
        self.cursor.execute("""SHOW COLUMNS FROM Enominado""")
        campos = self.cursor.fetchall()
        data = {}
        for value in campos:
            data[value[0]] = get_input(f"Informe o {value[0]} que é do tipo {value[1]}: ");
        self.inserir(data)


    def inserir (self, data: dict):

        query_data = (data['Premio'], data['Filme'], data['Pessoa'], data['Ganhou']);

        query = """INSERT INTO ENominado(Premio, Filme, Pessoa, Ganhou)
                    Values(%s, %s, %s, %s)""";

        self.cursor.execute(query, query_data);
        self.con.commit();

    def select_premio(self, cod_premio: int):
        query = f"""SELECT Pessoa, Ganhou FROM Enominado WHERE CodPremio = {cod_premio}""";
        self.cursor.execute(query);
        return self.cursor.fetchall();

    def select_questao_2b_4(self):
        query = """ SELECT DISTINCT E.Pessoa as Ator
                        FROM ENominado E, Premio P
                        WHERE E.CodPremio = P.CodPremio
                        AND E.Pessoa IN (
                            SELECT Pessoa FROM Premio, Enominado WHERE Enominado.CodPremio = Premio.CodPremio AND Premio.Nome = 'Oscar'
                        )
                        AND E.Pessoa IN (
                            SELECT Pessoa FROM Premio, Enominado WHERE Enominado.CodPremio = Premio.CodPremio AND Premio.Nome = 'Bafta'
                        )
                        AND E.Pessoa IN (
                            SELECT Pessoa FROM Premio, Enominado WHERE Enominado.CodPremio = Premio.CodPremio AND Premio.Nome = 'Golden Globe'
                        )
                        GROUP BY Ator
                """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def select_all(self):
        self.cursor.execute("""SELECT * FROM enominado""")
        return self.cursor.fetchall();
