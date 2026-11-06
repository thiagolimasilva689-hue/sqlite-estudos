import sqlite3
import csv
# Conectar ao banco
conexao = sqlite3.connect('minha_lista_compras.db')
cursor = conexao.cursor()

#criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS estoque  (
       data TEXT,
       produto TEXT,
       quantidade INT,
       valor FLOAT
    )
''')
# LER O CSV
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\produtos_mercado.csv'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho
    for linha in leitor:
     if len(linha) == 4: # CONTAR SE NUMEROS DE LINHAS ESTÁ CORRETO
        cursor.execute("INSERT INTO estoque VALUES (?, ?, ?, ?)",
                       (linha[0], linha[1], int(linha[2]), float(linha[3])))
    conexao.commit()
                       
"""
1)Qual o total de vendas (valor) por produto?

"""
cursor.execute('''
SELECT produto,SUM(valor) as total
from estoque 
group by produto
''')
for produto,total in cursor.fetchall():
    print(f"{produto}: R$ {total:.2f}")

"""
Qual o total de vendas por dia?
"""
cursor.execute('''
SELECT data,SUM(valor) as total
from estoque 
group by data
''')
for data,total in cursor.fetchall():
    print(f"{data}: R$ {total:.2f}")

"""
Qual o produto mais vendido (em quantidade total)?
"""
cursor.execute('''
SELECT produto,SUM(quantidade) as comprado
from estoque 
group by produto
ORDER BY comprado  DESC
limit 1
''')
vendas = cursor.fetchone()
print(f"O MAIS COMPRADO FOI: { vendas[0] }")
  

"""
6 — Quantos produtos diferentes
"""
cursor.execute('SELECT COUNT(DISTINCT produto) FROM estoque')
total = cursor.fetchone()[0]
print(f"Produtos diferentes: {total}")

"""
7)FATURAMENTO
"""
cursor.execute('SELECT SUM(valor) FROM estoque')
total = cursor.fetchone()[0]
print(f"Valor total: R$ {total:.2f}")

"""8) media de valores"""
cursor.execute('SELECT produto,AVG(valor)as media FROM estoque group by produto')
media = cursor.fetchone()
for produto, media in cursor.fetchall():
    print(f"{produto}: R$ {media:.2f}")
