import csv
import sqlite3
# Conectar ao banco
conexao = sqlite3.connect('Meu_zoologico.db')
cursor = conexao.cursor()

#criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS animais  (
        nome  TEXT,
        especie TEXT,
        idade INTEGER,
        peso FLOAT,
        estado_emocional TEXT 
    )
''')
# LER O CSV
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\zoologico.csv'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho

    for linha in leitor:
        cursor.execute("INSERT INTO animais VALUES (?, ?, ?, ?, ?)", 
                     (linha[0], linha[1], int(linha[2]), float(linha[3]), linha[4]))
        
# CONSULTAS
"""
Consulta 1 — Animais com fome
Mostre todos os animais que estão com estado_emocional = 'fome'.
"""
#cursor.execute('SELECT * FROM animais WHERE estado_emocional  ="fome"')
#for linha in cursor.fetchall():
 #     print(linha)   

"""
 Consulta 2 — Animais pesados
Mostre nome e peso dos animais com peso > 100, ordenados do mais pesado para o mais leve.
 
"""
#cursor.execute('''
 #   SELECT nome, peso 
  #  FROM animais 
   # WHERE peso > 100 
    #ORDER BY peso DESC
#''')
#for linha in cursor.fetchall():
 #   print(linha)
    
"""
Consulta 3 — Média de idade
Mostre a idade média de todos os animais.
"""
#cursor.execute('SELECT AVG(idade) FROM animais')
#media = cursor.fetchone()[0]
#print(f"Média de idade: {media:.1f} anos") 

"""
Consulta 4 — Animais jovens
Mostre nome, espécie e idade dos animais com idade < 10, ordenados do mais novo para o mais velho.
"""
#novos = cursor.execute('''
 #   SELECT nome, especie, idade
  #  FROM animais 
   # WHERE idade < 10
    #ORDER BY idade ASC
#''')
#for nome,especie,idade  in novos: 
 #  print(f"{nome} | {especie} | {idade}")

"""
 Consulta 5 — Relatório final
Mostre:

Quantos animais no total

Animal mais velho (nome e idade)

Animal mais novo (nome e idade)

Peso médio de todos os animais
 
 """
#Quantos animais no total
#cursor.execute('SELECT COUNT(*) FROM animais')
#total = cursor.fetchone()[0]
#print(f"EXISTEM AO TUDO : {total}") 

#cursor.execute('SELECT nome, idade FROM animais ORDER BY idade DESC LIMIT 1FROM animais')
#velho = cursor.fetchone()[0]
#print(f"O maior velho de tudos: {velho}")

#Animal mais novo (nome e idade)
#cursor.execute('SELECT nome, idade FROM animais ORDER BY idade ASC LIMIT 1 FROM animais')
#novo = cursor.fetchone()[0]
#print(f"O mais novinho(a) de tudos é : {novo}")


#Peso médio de todos os animais
cursor.execute('SELECT AVG(peso) FROM animais')
medio = cursor.fetchone()[0]
print(f"O peso medio de tudos é : {medio:.1f} KG")

    
