create database trabalho_bd1;
use trabalho_bd1;

-- criação das tabelas (com chave primaria)

create table Premio(
   CodPremio INT PRIMARY KEY AUTO_INCREMENT,
   Tipo		VARCHAR(50)		NOT NULL
  ,Nome		varchar(100)	NOT NULL
  ,Check (tipo in ("melhor ator principal"
					,"melhor atriz principal"
                    ,"melhor ator coadjuvante"
                    ,"melhor atriz coadjuvante"
                    ,"melhor filme"
                    ,"melhor direção"))
);
create table Eventos(
   Nome				varchar(100)	primary key
  ,Ano				int(4)			NOT NULL
  ,Nacionalidade	varchar(50)		NOT NULL
  ,Tipo				varchar(8)		,Check ( Tipo in ("academia"
														,"festival"
														,"concurso"))
  ,AnoInicio		char(4)			NOT NULL
);
create table Edicao(
   Ano				int(4)		primary key
  ,Data				date			NOT NULL
  ,Localizacao		varchar(50)		NOT NULL
  ,Premio			INT	NOT NULL
);
create table Filmes(
   idFilme				varchar(60)		primary key
  ,AnoProducao			int(4)			NOT NULL
  ,TituloOriginal		varchar(50)		NOT NULL
  ,DataEstreia			date			NOT NULL
  ,TituloNoBrasil		varchar(100)
  ,ArrecadacaoPrimAno	decimal(13, 2)
  ,LocaisEstreia		varchar(50)		NOT NULL
  ,Classe				varchar(12)		NOT NULL	check( Classe in ("comedia"
																		,"musical"
																		,"terror"
																		,"documentario",
                                                                        "drama"))
);
create table FilmeNominado(
   Premio		INT	NOT NULL
  ,Filme		varchar(60)		NOT NULL
  ,Premiado		varchar(50)		NOT NULL
);
create table Pessoa(
   NomeArt			varchar(50)		primary key
  ,NomeVerd			varchar(100)	NOT NULL
  ,Sexo				char(1) 		NOT NULL	Check ( Sexo in ("F"
																,"M"))
  ,AnoNasc			int(4)			NOT NULL
  ,Site				varchar(100)	NOT NULL
  ,AnoInic			int(4)			NOT NULL
  ,Situacao			varchar(10)		NOT NULL	Check ( Situacao in ("ativo"
																	,"aposentado"
                                                                    ,"falecido"))
  ,NroTotalAnos		int(10)			NOT NULL
);
create table EJuri(
   Ano		int(4)			NOT NULL
  ,Nome		varchar(50)		NOT NULL
);
create table ENominado(
   CodPremio		INT	NOT NULL
  ,Filme		varchar(60)		NOT NULL
  ,Pessoa		varchar(50)		NOT NULL
  ,Ganhou		char(1)			NOT NULL	check (ganhou in ("0","1"))
);
create table LocalEstreia(
   Sala		int(2)			NOT NULL
  ,Cinema	varchar(30)		NOT NULL
  ,IdLocal	varchar(50)		primary key
);
create table Documentario(
   IdFilme		varchar(60)		NOT NULL
  ,Nome			varchar(50)		NOT NULL
);
create table Outros(
   IdFilme	varchar(60)		primary key
  ,Nome		varchar(50)		NOT NULL
);
create table Diretor(
   Nome		varchar(60)		primary key
  ,Cargos	varchar(20)		NOT NULL
);
create table Produtor(
   Nome		varchar(60)		primary key
  ,Cargos	varchar(20)		NOT NULL
);
create table Roteirista(
   Nome		varchar(60)		primary key
  ,Cargos	varchar(20)		NOT NULL
);
create table Ator(
   Nome		varchar(60)		primary key
  ,Cargos	varchar(20)		NOT NULL
);
create table ERoteirista(
   Filme		varchar(60)		NOT NULL
  ,Roteirista	varchar(30)		NOT NULL
);
create table EProdutor(
   Filme		varchar(60)		NOT NULL
  ,Produtor		varchar(30)		NOT NULL
);
create table AtorElenco(
   Filme	varchar(60)		NOT NULL
  ,Atores	varchar(30)		NOT NULL
);
create table AtorPrinc(
   Filme	varchar(60)		NOT NULL
  ,Ator		varchar(30)		NOT NULL
);
create table EDiretor(
   Filme	varchar(60)		NOT NULL
  ,Diretor	varchar(30)		NOT NULL
);

-- alteração para adicionar as chaves secundarias

alter table eventos
add constraint foreign key (ano) references Edicao(ano)
on delete cascade
on update cascade;

ALTER TABLE ejuri
ADD FOREIGN KEY (ano) REFERENCES edicao(ano)
on delete cascade
on update cascade
;

ALTER TABLE ejuri
ADD constraint FOREIGN KEY (nome) REFERENCES pessoa(nomeArt)
on delete cascade
on update cascade
;

ALTER TABLE edicao
ADD constraint FOREIGN KEY (premio) REFERENCES premio(CodPremio)
on delete cascade
on update cascade
;

ALTER TABLE filmeNominado
ADD constraint FOREIGN KEY (premio) REFERENCES premio(CodPremio)
on delete cascade
on update cascade
;

ALTER TABLE ENominado
ADD constraint FOREIGN KEY (CodPremio) REFERENCES premio(CodPremio)
on delete cascade
on update cascade
;

ALTER TABLE filmeNominado
ADD constraint FOREIGN KEY (filme) REFERENCES Filmes(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE ENominado
ADD constraint FOREIGN KEY (filme) REFERENCES Filmes(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE Documentario
ADD constraint FOREIGN KEY (idFilme) REFERENCES Filmes(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE Outros
ADD constraint FOREIGN KEY (idFilme) REFERENCES Filmes(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE AtorElenco
ADD constraint FOREIGN KEY (Filme) REFERENCES Outros(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE AtorPrinc
ADD constraint FOREIGN KEY (Filme) REFERENCES Outros(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE ERoteirista
ADD constraint FOREIGN KEY (Filme) REFERENCES Filmes(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE EProdutor
ADD constraint FOREIGN KEY (Filme) REFERENCES Filmes(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE EDiretor
ADD constraint FOREIGN KEY (Filme) REFERENCES Filmes(idFilme)
on delete cascade
on update cascade
;

ALTER TABLE Filmes
ADD constraint FOREIGN KEY (LocaisEstreia) REFERENCES LocalEstreia(idLocal)
on delete cascade
on update cascade
;

ALTER TABLE ENominado
ADD constraint FOREIGN KEY (Pessoa) REFERENCES Pessoa(NomeArt)
on delete cascade
on update cascade
;

ALTER TABLE Diretor
ADD constraint FOREIGN KEY (Nome) REFERENCES Pessoa(NomeArt)
on delete cascade
on update cascade
;

ALTER TABLE Produtor
ADD constraint FOREIGN KEY (Nome) REFERENCES Pessoa(NomeArt)
on delete cascade
on update cascade
;

ALTER TABLE Roteirista
ADD constraint FOREIGN KEY (Nome) REFERENCES Pessoa(NomeArt)
on delete cascade
on update cascade
;

ALTER TABLE Ator
ADD constraint FOREIGN KEY (Nome) REFERENCES Pessoa(NomeArt)
on delete cascade
on update cascade
;

ALTER TABLE ERoteirista
ADD constraint FOREIGN KEY (Roteirista) REFERENCES Roteirista(Nome)
on delete cascade
on update cascade
;

ALTER TABLE EProdutor
ADD constraint FOREIGN KEY (Produtor) REFERENCES Produtor(Nome)
on delete cascade
on update cascade
;

ALTER TABLE AtorElenco
ADD constraint FOREIGN KEY (Atores) REFERENCES Ator(Nome)
on delete cascade
on update cascade
;

ALTER TABLE AtorPrinc
ADD constraint FOREIGN KEY (Ator) REFERENCES Ator(Nome)
on delete cascade
on update cascade
;

ALTER TABLE EDiretor
ADD constraint FOREIGN KEY (Diretor) REFERENCES Diretor(Nome)
on delete cascade
on update cascade
;

-- item 1:
-- a)
DELIMITER //
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
DELIMITER ;


-- b)
DELIMITER //
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
    SET MESSAGE_TEXT = 'Inserção em AtorElenco não permitida.';
  END IF;
END;
//
DELIMITER ;

INSERT INTO premio (Tipo, Nome) VALUES
('melhor ator principal', 'Oscar'),
('melhor atriz principal', 'Oscar'),
('melhor ator coadjuvante', 'Oscar'),
('melhor atriz coadjuvante', 'Oscar'),
('melhor filme', 'Oscar'),
('melhor direção', 'Oscar'),
('melhor ator principal', 'Bafta'),
('melhor atriz principal', 'Bafta'),
('melhor ator coadjuvante', 'Bafta'),
('melhor atriz coadjuvante', 'Bafta'),
('melhor filme', 'Bafta'),
('melhor direção', 'Bafta'),
('melhor ator principal', 'Golden Globe'),
('melhor atriz principal', 'Golden Globe'),
('melhor ator coadjuvante', 'Golden Globe'),
('melhor atriz coadjuvante', 'Golden Globe'),
('melhor filme', 'Golden Globe'),
('Melhor Direção', 'Golden Globe');

INSERT INTO localestreia (Sala, Cinema, IdLocal) VALUES
(3, 'Franco da Rocha', 'Estados Unidos');

INSERT INTO filmes (idFilme, AnoProducao, TituloOriginal, DataEstreia, TituloNoBrasil, ArrecadacaoPrimAno, LocaisEstreia, Classe) VALUES
('FILME01', 2019, 'Joker', "2019-10-4", 'Coringa', 1074.30, 'Estados Unidos', 'Drama'),
('FILME02', 2019, 'The Lighthouse', "2019-10-18", 'O Farol', 18.08, 'Estados Unidos', 'Terror'),
('FILME03', 2019, 'Once Upon a Time in Hollywood', "2019-7-26", 'Era Uma Vez em... Hollywood', 374.33, 'Estados Unidos', 'Drama'),
('FILME04', 2019, 'Marriage Story', "2019-12-6", 'História de um Casamento', 2.29, 'Estados Unidos', 'Drama'),
('FILME05', 2019, 'The Farewell', "2019-7-12", 'A Despedida', 22.46, 'Estados Unidos', 'Drama'),
('FILME06', 2019, 'Little Women', "2019-12-25", 'Adoráveis Mulheres', 209.04, 'Estados Unidos', 'Drama'),
('FILME07', 2019, 'Jojo Rabbit', "2019-12-25", 'Jojo Rabbit', 90.33, 'Estados Unidos', 'Comédia'),
('FILME08', 2019, 'Portrait of a Lady on Fire', "2019-9-18", 'Retrato de uma Jovem em Chamas', 22.42, 'Estados Unidos', 'Drama'),
('FILME09', 2019, 'The Irishman', "2019-11-27", 'O Irlandês', 8.91, 'Estados Unidos', 'Drama'),
('FILME10', 2019, 'Once Upon a Time in Hollywood', "2019-7-26", 'Era Uma Vez em... Hollywood', 374.33, 'Estados Unidos', 'Drama'),
('FILME11', 2019, 'The Lion King', "2019-7-18", 'O Rei Leão', 1656.94, 'Estados Unidos', 'Musical'),
('FILME12', 2019, 'Toy Story 4', "2019-6-20", 'Toy Story 4', 1074.17, 'Estados Unidos', 'Musical'),
('FILME13', 2019, 'Ford v Ferrari', "2019-11-15", 'Ford vs Ferrari', 225.51, 'Estados Unidos', 'Drama'),
('FILME14', 2018, 'A Quiet Place', "2018-4-5", 'Um Lugar Silencioso', 340.95, 'Estados Unidos', 'Terror'),
('FILME15', 2018, 'BlacKkKlansman', "2018-8-10", 'Infiltrado na Klan', 93.42, 'Estados Unidos', 'Drama'),
('FILME16', 2018, 'The Favourite', "2019-1-24", 'A Favorita', 95.98, 'Estados Unidos', 'Drama'),
('FILME17', 2018, 'Green Book', "2019-1-10", 'Green Book: O Guia', 320.71, 'Estados Unidos', 'Drama');

INSERT INTO pessoa (NomeArt, NomeVerd, Sexo, AnoNasc, Site, AnoInic, Situacao, NrOTotalAnos) VALUES
('Adam Driver', 'Adam Driver', 'M', 1983, 'www.adamdriversite.com', 2009, 'Ativo', 14),
('Adèle Haenel', 'Adèle Haenel', 'F', 1989, 'www.adelehaenelsite.com', 2002, 'Ativo', 21),
('Al Pacino', 'Alfredo James Pacino', 'M', 1940, 'www.alpacinosite.com', 1967, 'Ativo', 56),
('Allison Janney', 'Allison Janney', 'F', 1975, 'https://www.allisonjanney.com/', 1991, 'Ativo', 25),
('Annie Potts', 'Annie Potts', 'F', 1952, 'www.anniepottssite.com', 1976, 'Ativo', 47),
('Awkwafina', 'Nora Lum', 'F', 1988, 'www.awkwafinasite.com', 2011, 'Ativo', 12),
('Beyoncé', 'Beyoncé Giselle Knowles-Carter', 'F', 1981, 'www.beyoncesite.com', 1997, 'Ativo', 26),
('Brad Pitt', 'Brad Pitt', 'M', 1963, 'www.bradpittsite.com', 1987, 'Ativo', 36),
('Chiwetel Ejiofor', 'Chiwetel Ejiofor', 'M', 1977, 'www.chiwetelejioforsite.com', 1995, 'Ativo', 28),
('Christian Bale', 'Christian Bale', 'M', 1974, 'www.christianbalesite.com', 1986, 'Ativo', 37),
('Donald Glover', 'Donald Glover', 'M', 1983, 'www.donaldgloversite.com', 2002, 'Ativo', 21),
('Eliza Scanlen', 'Eliza Scanlen', 'F', 1999, 'www.elizascanlensite.com', 2015, 'Ativo', 8),
('Emma Watson', 'Emma Watson', 'F', 1990, 'www.emmawatsonsite.com', 2001, 'Ativo', 22),
('Florence Pugh', 'Florence Pugh', 'F', 1996, 'www.florencepughsite.com', 2014, 'Ativo', 9),
('Frances Conroy', 'Frances Conroy', 'F', 1953, 'www.francesconroysite.com', 1976, 'Ativo', 47),
('Frances McDormand', 'Frances McDormand', 'F', 1957, 'https://www.francesmcguire.com/', 1984, 'Ativo', 40),
('Gary Oldman', 'Gary Oldman', 'M', 1958, 'https://www.garyoldman.com/', 1985, 'Ativo', 35),
('Glenn Close', 'Glenn Close', 'F', 1947, 'https://www.glennclose.com/', 1974, 'Ativo', 45),
('James Earl Jones', 'James Earl Jones', 'M', 1931, 'www.jamesearljonessite.com', 1953, 'Ativo', 70),
('Joe Pesci', 'Joe Pesci', 'M', 1943, 'www.joepescisite.com', 1961, 'Ativo', 62),
('Jordan Peele', 'Jordan Peele', 'M', 1979, 'www.jordanpeelesite.com', 2003, 'Ativo', 20),
('Keegan-Michael Key', 'Keegan-Michael Key', 'M', 1971, 'www.keeganmichaelkeysite.com', 2001, 'Ativo', 22),
('Laura Dern', 'Laura Dern', 'F', 1967, 'www.lauradernsite.com', 1973, 'Ativo', 50),
('Leonardo DiCaprio', 'Leonardo DiCaprio', 'M', 1974, 'www.leonardodicapriosite.com', 1989, 'Ativo', 34),
('Mahershala Ali', 'Mahershala Ali', 'M', 1971, 'https://www.mahershalaali.com/', 2000, 'Ativo', 20),
('Margot Robbie', 'Margot Robbie', 'F', 1990, 'www.margotrobbiesite.com', 2008, 'Ativo', 15),
('Matt Damon', 'Matt Damon', 'M', 1970, 'www.mattdamonsite.com', 1988, 'Ativo', 35),
('Meryl Streep', 'Meryl Streep', 'F', 1949, 'www.merylstreepsite.com', 1975, 'Ativo', 48),
('Noémie Merlant', 'Noémie Merlant', 'F', 1988, 'www.noemiemerlantsite.com', 2008, 'Ativo', 15),
('Olivia Colman', 'Olivia Colman', 'F', 1974, 'https://www.oliviacolman.com/', 2001, 'Ativo', 20),
('Rachel Weisz', 'Rachel Weisz', 'F', 1971, 'https://www.rachelweisz.com/', 1995, 'Ativo', 25),
('Rami Malek', 'Rami Malek', 'M', 1981, 'https://www.ramimalek.com/', 2004, 'Ativo', 10),
('Regina King', 'Regina King', 'F', 1971, 'https://www.reginaking.com/', 1995, 'Ativo', 25),
('Robert De Niro', 'Robert De Niro', 'M', 1943, 'www.robertdenirosite.com', 1965, 'Ativo', 58),
('Robert Pattinson', 'Robert Pattinson', 'M', 1986, 'www.robertpattinsonsite.com', 2004, 'Ativo', 19),
('Roman Griffin Davis', 'Roman Griffin Davis', 'M', 2007, 'www.romangriffindavissite.com', 2019, 'Ativo', 4),
('Sam Rockwell', 'Sam Rockwell', 'M', 1968, 'www.samrockwellsite.com', 1989, 'Ativo', 34),
('Saoirse Ronan', 'Saoirse Ronan', 'F', 1994, 'www.saoirseronansite.com', 2003, 'Ativo', 20),
('Scarlett Johansson', 'Scarlett Johansson', 'F', 1984, 'www.scarlettjohanssonsite.com', 1994, 'Ativo', 29),
('Taika Waititi', 'Taika Waititi', 'M', 1975, 'www.taikawaititisite.com', 1999, 'Ativo', 24),
('Thomasin McKenzie', 'Thomasin McKenzie', 'F', 2000, 'www.thomasinmckenziesite.com', 2015, 'Ativo', 8),
('Tim Allen', 'Tim Allen', 'M', 1953, 'www.timallensite.com', 1975, 'Ativo', 48),
('Timothée Chalamet', 'Timothée Chalamet', 'M', 1995, 'www.timotheechalametsite.com', 2014, 'Ativo', 9),
('Tom Hanks', 'Tom Hanks', 'M', 1956, 'www.tomhankssite.com', 1977, 'Ativo', 46),
('Tony Hale', 'Tony Hale', 'M', 1970, 'www.tonyhalesite.com', 1997, 'Ativo', 26),
('Willem Dafoe', 'Willem Dafoe', 'M', 1955, 'www.willemdafoesite.com', 1979, 'Ativo', 44),
('Zazie Beetz', 'Zazie Beetz', 'F', 1991, 'www.zaziebeetzsite.com', 2013, 'Ativo', 10),
('Zhao Shuzhen', 'Zhao Shuzhen', 'F', 1945, 'www.zhaoshuzhensite.com', 2019, 'Ativo', 4);

INSERT INTO filmenominado (Premio, Filme, Premiado) VALUES
(5, 'FILME01', '0'),
(6, 'FILME01', '0'),
(5, 'FILME02', '0'),
(6, 'FILME02', '0'),
(11, 'FILME03', '1'),
(12, 'FILME03', '0'),
(5, 'FILME04', '0'),
(6, 'FILME04', '0'),
(5, 'FILME05', '0'),
(6, 'FILME05', '0'),
(5, 'FILME06', '0'),
(6, 'FILME06', '0'),
(6, 'FILME07', '1'),
(5, 'FILME08', '0'),
(6, 'FILME08', '0'),
(5, 'FILME09', '0'),
(6, 'FILME09', '0'),
(5, 'FILME11', '0'),
(6, 'FILME11', '0'),
(5, 'FILME12', '1'),
(11, 'FILME12', '0'),
(17, 'FILME13', '0'),
(17, 'FILME14', '0'),
(11, 'FILME15', '0'),
(12, 'FILME15', '0'),
(11, 'FILME16', '1'),
(12, 'FILME16', '0'),
(5, 'FILME17', '1'),
(5, 'FILME01', '0'),
(5, 'FILME12', '1'),
(5, 'FILME04', '0'),
(6, 'FILME03', '1'),
(6, 'FILME06', '0'),
(6, 'FILME15', '0'),
(11, 'FILME07', '1'),
(11, 'FILME16', '0'),
(11, 'FILME02', '0'),
(12, 'FILME09', '1'),
(12, 'FILME11', '0'),
(12, 'FILME06', '0'),
(17, 'FILME04', '1'),
(17, 'FILME08', '0'),
(17, 'FILME09', '0'),
(10, 'FILME03', '0'),
(10, 'FILME09', '1'),
(10, 'FILME16', '0'),
(11, 'FILME13', '1'),
(11, 'FILME14', '0'),
(11, 'FILME17', '0'),
(12, 'FILME15', '0'),
(12, 'FILME04', '1'),
(12, 'FILME05', '0'),
(13, 'FILME06', '0'),
(13, 'FILME11', '1'),
(13, 'FILME02', '0'),
(14, 'FILME03', '1'),
(14, 'FILME09', '0'),
(14, 'FILME01', '0'),
(10, 'FILME03', '1'),
(10, 'FILME09', '1'),
(10, 'FILME16', '1'),
(10, 'FILME01', '1');

INSERT INTO enominado (CodPremio, Filme, Pessoa, Ganhou) VALUES
(1, 'FILME01', 'Adam Driver', '0'),
(3, 'FILME03', 'Al Pacino', '0'),
(2, 'FILME02', 'Adèle Haenel', '0'),
(3, 'FILME03', 'Al Pacino', '0'),
(4, 'FILME04', 'Allison Janney', '0'),
(5, 'FILME05', 'Annie Potts', '0'),
(6, 'FILME06', 'Awkwafina', '0'),
(7, 'FILME07', 'Beyoncé', '0'),
(8, 'FILME08', 'Brad Pitt', '0'),
(9, 'FILME09', 'Chiwetel Ejiofor', '0'),
(10, 'FILME10', 'Christian Bale', '0'),
(11, 'FILME16', 'Frances McDormand', '1'),
(12, 'FILME17', 'Gary Oldman', '1'),
(13, 'FILME01', 'Glenn Close', '1'),
(14, 'FILME02', 'James Earl Jones', '1'),
(15, 'FILME03', 'Joe Pesci', '1'),
(7, 'FILME02', 'Adam Driver', '0'),
(13, 'FILME02', 'Adam Driver', '1'),
(1, 'FILME01', 'Willem Dafoe', '1'),
(1, 'FILME12', 'Tom Hanks', '0'),
(1, 'FILME04', 'Gary Oldman', '0'),
(2, 'FILME03', 'Scarlett Johansson', '0'),
(2, 'FILME06', 'Saoirse Ronan', '1'),
(2, 'FILME15', 'Emma Watson', '0'),
(3, 'FILME02', 'Brad Pitt', '0'),
(3, 'FILME05', 'Chiwetel Ejiofor', '1'),
(3, 'FILME11', 'Matt Damon', '0'),
(4, 'FILME07', 'Laura Dern', '1'),
(4, 'FILME10', 'Margot Robbie', '0'),
(4, 'FILME14', 'Frances Conroy', '0'),
(7, 'FILME02', 'Brad Pitt', '0'),
(7, 'FILME05', 'Chiwetel Ejiofor', '1'),
(7, 'FILME11', 'Matt Damon', '0'),
(8, 'FILME07', 'Laura Dern', '0'),
(8, 'FILME10', 'Margot Robbie', '1'),
(8, 'FILME14', 'Frances Conroy', '0'),
(9, 'FILME01', 'Willem Dafoe', '1'),
(9, 'FILME12', 'Tom Hanks', '0'),
(9, 'FILME04', 'Gary Oldman', '0'),
(10, 'FILME02', 'Margot Robbie', '1'),
(10, 'FILME06', 'Meryl Streep', '0'),
(10, 'FILME17', 'Olivia Colman', '0'),
(13, 'FILME13', 'Matt Damon', '1'),
(13, 'FILME14', 'Robert Pattinson', '0'),
(13, 'FILME04', 'Jordan Peele', '0'),
(14, 'FILME14', 'Saoirse Ronan', '1'),
(14, 'FILME16', 'Olivia Colman', '0'),
(14, 'FILME04', 'Noémie Merlant', '0'),
(15, 'FILME07', 'Chiwetel Ejiofor', '1'),
(15, 'FILME08', 'Brad Pitt', '0'),
(15, 'FILME13', 'Matt Damon', '0'),
(16, 'FILME02', 'Emma Watson', '1'),
(16, 'FILME16', 'Olivia Colman', '0'),
(16, 'FILME09', 'Eliza Scanlen', '0');