import csv
import sqlite3

conexao = sqlite3.connect('estudos.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM materias')
dados = cursor.fetchall()

with open('materias.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(['Nome', 'Horas', 'Dificuldade', 'Status'])
    escritor.writerows(dados)

print("Arquivo materias.csv criado!")
conexao.close()