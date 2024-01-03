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
    
    
    def Questao2_B_3 (self): ## Gerar um gráfico, histograma, que apresente os 10 filmes com maior arrecadação
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


    def Questao2_B_4 (self): ## listar os atores (atrizes) nominados como melhor ator em todos os eventos existentes”.
        consulta_sql = """SELECT NomeArt
                         FROM ENominado EN, Premio PR
                            WHERE EN.CodPremio = PR.CodPremio
                                AND (PR.TipoPremio in ('melhor ator principal', 'melhor atriz principal', 'melhor ator coadjuvante',
                                                        'melhor atriz coadjuvante')
                         ORDER BY NomeArt
                         """
        
    def Questao2_B_5 (self): ## dado um prêmio, indique quais foram os autores ou filmes nominados e premiados.
        
        consulta_sql = "SELECT * FROM Premio"
        total_premios = "SELECT CodPremio FROM Premio"

        print(consulta_sql)
        ''' premio = input("""
                          01    |  Melhor Ator Principal        | Oscar 
                          02    |  Melhor Atriz Principal       | Oscar - enominado
                          03    |  Melhor Ator Coadjuvante      | Oscar - enominado
                          04    |  Melhor Atriz Coadjuvante     | Oscar - enominado
                          05    |  Melhor Filme                 | Oscar - filmeNominado
                          06    |  Melhor Direção               | Oscar - filmeNominado
                          07    |  Melhor Ator Principal        | Bafta - enominado
                          08    |  Melhor Atriz Principal       | Bafta - enominado
                          09    |  Melhor Ator Coadjuvante      | Bafta - enominado
                       
                          10    |  Melhor Atriz Coadjuvante     | Bafta - enominado
                          11    |  Melhor Filme                 | Bafta - filmeNominado
                          12    |  Melhor Direção               | Bafta - filmeNominado
                          13    |  Melhor Ator Principal        | Golden Globe - enominado
                          14    |  Melhor Atriz Principal       | Golden Globe - enominado
                          15    |  Melhor Ator Coadjuvante      | Golden Globe - enominado
                          16    |  Melhor Atriz Coadjuvante     | Golden Globe - enominado
                          17    |  Melhor Filme                 | Golden Globe - filmeNominado
                          18    |  Melhor Direção               | Golden Globe - filmeNominado
                       
                       Digite o código do premio conforme a tabela: 
                       """)
        '''

        premio = input("Digite o código do premio conforme a tabela: ")

        if(premio ):
            print("Código inválido")
            return;
        
        consulta_sql = f"""
                        SELECT Filme, Pessoa as Atores
                        FROM ENominado EN, FilmeNominado FN
                        WHERE EN.CodPremio = '{premio}' AND FN.CodPremio = '{premio}'
                        """
        
q = Questoes();
q.Questao2_B_5();

