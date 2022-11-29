/*EXECUTAR DENTRO DO MYSQL*/

/*Inserindo dados na tabela usuários*/
INSERT INTO usuarios (nome, nickname, senha) VALUES ("Paola Capita", "PaolaCa", "alohomora");
INSERT INTO usuarios (nome, nickname, senha) VALUES ('Breno M', 'Breno', 'PAPAPA');
INSERT INTO usuarios (nome, nickname, senha) VALUES ('Testizinho', 'TESTE', 'TESTE');

commit;

/*Inserindo dados na tabela jogos*/
INSERT INTO jogos (timeMandante,timeVisitante,grupo,placar,faltas,cartAmarelo,cartVermelho) VALUES ('Botafogo', 'Sala B', 'Atari', '4X1', 4, 3, 2);
INSERT INTO jogos (timeMandante,timeVisitante,grupo,placar,faltas,cartAmarelo,cartVermelho) VALUES ('4º A', 'Sala B', 'Atari', '0X1', 20, 0, 0);
INSERT INTO jogos (timeMandante,timeVisitante,grupo,placar,faltas,cartAmarelo,cartVermelho) VALUES ('Botafogo', '4º A', 'Atari', '0X0', 2, 3, 0);

commit;

/*Inserindo dados na tabela times*/
INSERT INTO times (nome,campeonato,qtdJogadores) VALUES ('Botafogo', 'Brasileirão Série B', 25);
INSERT INTO times (nome,campeonato,qtdJogadores) VALUES ('Sala B', 'Interclasse manhã', 13);
INSERT INTO times (nome,campeonato,qtdJogadores) VALUES ('4º A', 'Interclasse noite', 8);

commit;

/*Inserindo dados na tabela torcidas*/
INSERT INTO torcidas (nome, time, socios) VALUES ('Botas', 'Botafogo', 5000);
INSERT INTO torcidas (nome, time, socios) VALUES ('4tou', '4º A', 10);
INSERT INTO torcidas (nome, time, socios) VALUES ('BBs', 'Sala B', 15);

commit;

/*conferindo dados*/
SELECT *
FROM usuarios;

SELECT *
FROM jogos;

SELECT *
FROM times;

SELECT *
FROM torcidas;