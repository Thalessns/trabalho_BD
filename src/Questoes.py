import pandas as pd
import matplotlib.pyplot as plt
from database.db import connect;

class Questoes:
    def __init__(self):
        self.con = connect();
        self.cursor = self.con.cursor();

    def Questao2_B_1 (self): ## apresente os 10 atores com maior número de prêmios.
        consulta_sql = """SELECT NomeArt, count(Ganhou) as Premios
                         FROM Pessoa P, ENominado EN
                         WHERE P.NomeArt = EN.Pessoa
                            AND EN.Ganhou = '1'
                         GROUP BY NomeArt
                         ORDER BY Premios desc
                         LIMIT 10
                         """
        df = pd.read_sql(consulta_sql, self.con);

        df.plot(x='NomeArt', y='Premios', kind='bar', color='skyblue')
        plt.title('Top 10 Atores/Atrizes mais premiados')
        plt.xlabel('Atores/Atrizes')
        plt.ylabel('Qtd Prêmios')
        plt.show()

    def Questao2_B_2 (self): ## apresente os 10 filmes mais premiados. 
        consulta_sql = """
                        SELECT idFilme, TituloNoBrasil, count(Premiado) as Premios
                        FROM FilmeNominado FN, Filmes F
                        where FN.Filme = F.idFilme 
                        AND Premiado = '1'
                        GROUP BY idFilme
                        ORDER BY Premios desc
                        LIMIT 10
                        """
                        ## FROM Filmes
                         ## ORDER BY Premios desc
                         ## LIMIT 10
        
        df = pd.read_sql(consulta_sql, self.con);

        df.plot(x='TituloNoBrasil', y='Premios', kind='bar', color='skyblue')
        plt.title('Top 10 Filmes mais premiados')
        plt.xlabel('Filmes')
        plt.ylabel('Qtd Premios')
        plt.show()
    
    
    def Questao2_B_3 (self):
        consulta_sql = """SELECT TituloNoBrasil, ArrecadacaoPrimAno
                         FROM Filmes
                         ORDER BY ArrecadacaoPrimAno desc
                         LIMIT 10""" 

        df = pd.read_sql(consulta_sql, self.con);

        df.plot(x='TituloNoBrasil', y='ArrecadacaoPrimAno', kind='bar', color='skyblue')
        plt.title('Top 10 Filmes com Maiores Areecadações no Primeiro Ano de Lançamento')
        plt.xlabel('Filmes')
        plt.ylabel('Arrecadação (em milhões)')
        plt.show()

    def Questao2_B_4 (self):
        consulta_sql = """SELECT NomeArt
                         FROM ENominado EN, Premio PR
                            WHERE EN.CodPremio = PR.CodPremio
                                AND (PR.TipoPremio in ('melhor ator principal', 'melhor atriz principal', 'melhor ator coadjuvante',
                                                        'melhor atriz coadjuvante')
                         ORDER BY NomeArt
                         """

    

q = Questoes();
q.Questao2_B_1();

