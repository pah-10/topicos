# CRIA AS TABELAS DO BANCO AUTOMATICAMENTE

import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='S3nh@BanC00D@D0ss'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
      CREATE TABLE `jogos` (
      `idJogo` int(11) NOT NULL AUTO_INCREMENT,
      `timeMandante` varchar(50) NOT NULL,
      `timeVisitante` varchar(50) NOT NULL,
      `grupo` varchar(40) NOT NULL,
      `placar` varchar(20) NOT NULL,
      `faltas` int(100) NOT NULL,
      `cartAmarelo` int(100) NOT NULL,
      `cartVermelho` int(100) NOT NULL,
      PRIMARY KEY (`idJogo`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Times'] = ('''
      CREATE TABLE `times` (
      `idTime` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `campeonato` varchar(100) NOT NULL,
      `qtdJogadores` int(50) NOT NULL,
      PRIMARY KEY (`idTime`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Torcidas'] = ('''
      CREATE TABLE `torcidas` (
      `idTorcida` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `time` varchar(100) NOT NULL,
      `socios` int(50) NOT NULL,
      PRIMARY KEY (`idTorcida`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nome` varchar(50) NOT NULL,
      `nickname` varchar(10) NOT NULL,
      `senha` varchar(100) NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# commitando para gravar dados no banco
conn.commit()
cursor.close()
conn.close()
