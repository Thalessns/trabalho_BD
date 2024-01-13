import pandas as pd
from utils import print_table, clear, bars, menu, get_input;
import matplotlib.pyplot as plt
from database.db import connect;
from database.pessoa import Pessoa;
from database.filme import Filme;
from database.evento import Evento;
from database.premio import Premio;
from database.enominado import Enominado;
from database.filmenominado import FilmeNominado;

class Questoes:
    def __init__(self):
        self.con = connect();
        self.cursor = self.con.cursor();

    def Questao1_A(self):
        bars(size=100)
        print("""DELIMITER //
                CREATE TRIGGER before_insert_ejuri
                BEFORE INSERT ON ejuri
                FOR EACH ROW
                BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM enominado
                    WHERE pessoa = NEW.nome
                ) THEN
                    SIGNAL SQLSTATE '45000'
                    SET MESSAGE_TEXT = 'Inserção em ejuri não permitida. (Uma pessoa não pode ser júri de um Evento se participar de um filme aí indicado, com qualquer papel)';
                END IF;
                END;
                //
                DELIMITER;
        """)
        bars(size=100)
        input("Pressione ENTER para continuar...")
        
    def Questao1_B(self):
        bars(size=100)
        print("""DELIMITER //
            CREATE TRIGGER before_insert_AtorElenco
            BEFORE INSERT ON AtorElenco
            FOR EACH ROW
            BEGIN
            IF EXISTS (
                SELECT 1
                FROM Filmes
                WHERE IdFilme = NEW.Filme and classe = 'documentario'
            ) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Inserção em AtorElenco não permitida.';
            END IF;
            END;
            //
            DELIMITER ;

            DELIMITER //
            CREATE TRIGGER before_insert_AtorPrinc
            BEFORE INSERT ON AtorPrinc
            FOR EACH ROW
            BEGIN
            IF EXISTS (
                SELECT 1
                FROM Filmes
                WHERE IdFilme = NEW.Filme and classe = 'documentario'
            ) THEN
                SIGNAL SQLSTATE '45000'
                SET MESSAGE_TEXT = 'Inserção em AtorPrinc não permitida.';
            END IF;
            END;
            //
            DELIMITER ;
        """)
        bars(size=100)
        input("Pressione ENTER para continuar...")

    def Quastao2_A(self):
        opcoes = ["Sair", "Pessoa", "Filme", "Evento", "Premio", "Pessoas Indicadas", "Filmes Indicados"]
        
        while True:
            # Limpando tela
            clear()
            # Mostrando menu
            menu(title="Menu de Cadastro", params=opcoes)
            # Pegando opção do usuário
            escolha = get_input("Escolha uma das opções acima, pelo número listado: ")
            # Verificando opções escolhidas
            if (escolha.isdigit()) and (int(escolha) in range(0, len(opcoes))):
                escolha = int(escolha)
                if escolha == 0: 
                    print("Saindo...")
                    bars(size=50)
                    return
                elif escolha == 1:
                    p = Pessoa()
                    p.preparar_insercao()
                elif escolha == 2:
                    f = Filme()
                    f.preparar_insercao()
                elif escolha == 3:
                    e = Evento()
                    e.preparar_insercao()
                elif escolha == 4:
                    pr = Premio()
                    pr.preparar_insercao()
                elif escolha == 5:
                    en = Enominado()
                    en.preparar_insercao()
                elif escolha == 6:
                    fn = FilmeNominado()
                    fn.preparar_insercao()

            else:
                get_input(f"Por favor, digite um número válido [0, {len(opcoes)-1}]\nPRESS ENTER TO CONTINUE...")

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
        e = Enominado()
        resp = e.select_questao_2b_4()
        print_table(data=resp, columns=["Ator"], title="Atores e Atriz indicados como melhor ator em toos os eventos existentes")
        input("Pessione ENTER para continuar...")

        
    def Questao2_B_5 (self): ## dado um prêmio, indique quais foram os autores ou filmes nominados e premiados.
        
        p = Premio();
        while True:
            clear()
            print_table(data=p.select_all(), columns=["CodPremio", "Tipo", "Evento"], title="Tabela de Premios");

            premio = input("Digite o código do premio conforme a tabela [Digite 0 caso queira sair]: ");
            if premio.isdigit():
                premio = int(premio)
                tipo = p.select_tipo(cod_premio=premio)
                
                if premio == 0: return;
                elif ("ator" in tipo) or ("atriz" in tipo):
                    e = Enominado();
                    print_table(data=e.select_premio(cod_premio=premio), columns=["Pessoa", "Ganhou"], title="Tabela de Pessoas Indicadas");
                else:
                    f = FilmeNominado();
                    print_table(data=f.select_premio(codpremio=premio), columns=["Titulo Original", "Titulo Traduzido", "Premiado"], title="Tabela de Filmes Indicados");
            else:
                print("Por favor, escolha apenas numeros!")
            input("Pressione ENTER para continuar...")

