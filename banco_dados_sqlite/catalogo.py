import sqlite3
import csv

# Conectar ao banco
conexao = sqlite3.connect('catalogo')
cursor = conexao.cursor()

#criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        titulo TEXT,
        genero TEXT,
        ano INTEGER,
        nota REAL,
        status TEXT
    )
''')

# LER O CSV
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\ficção.csv'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho
    for linha in leitor:
     if len(linha) == 5: # CONTAR SE NUMEROS DE LINHAS ESTÁ CORRETO
        cursor.execute("INSERT INTO filmes VALUES (?, ?, ?, ?,?)",
                       (linha[0], linha[1], int(linha[2]), float(linha[3]),linha[4]))

#CONSULTAS

#Média de nota por gênero 
cursor.execute('SELECT AVG(nota) FROM filmes ')
media = cursor.fetchone()
print(f"A MEDIA DE CLASSIFIÇÃO DOS ITENS NO CATALOGO É  {media[0]:.2f}")

#Top 5 melhores notas 
cursor.execute('''
        SELECT  titulo, genero, ano, nota, status FROM filmes
        ORDER BY nota DESC
        LIMIT 5;
''')
for  titulo,genero,ano,nota,status in cursor.fetchall():
    print(f"{titulo} | {genero} | {ano} | {nota} | { status}")

"""Quantos filmes vs séries """

cursor.execute('''SELECT COUNT(genero) from filmes where genero = 'horror cósmico'
''')
cosmico= cursor.fetchone()
print(f"O NÚMERO DE GENERO QUE TEMER INSIGNIGENCIA DA HUMANIDADE : {cosmico[0]}")




