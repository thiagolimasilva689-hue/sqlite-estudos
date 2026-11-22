import sqlite3
conexao = sqlite3.connect('vendas.db')
cursor = conexao.cursor()
cursor.execute("""CREATE TABLE  IF NOT EXISTS vendas (
                  id INTEGER PRIMARY KEY,
                  produto TEXT NOT NULL,
                  categoria TEXT NOT NULL,
                  quantidade INTEGER NOT NULL,
                  preco_unitario REAL NOT NULL,
                  data_venda DATE NOT NULL
                  )""")
cursor.execute("SELECT COUNT(*) FROM vendas")
if cursor.fetchone()[0] == 0:
    cursor.executemany("""INSERT INTO vendas (produto, categoria, quantidade, preco_unitario, data_venda) VALUES (?, ?, ?, ?, ?)""", [
        ('Notebook Pro', 'Eletronicos', 2, 4500.00, '2026-01-15'),
        ('Mouse Gamer', 'Eletronicos', 10, 150.00, '2026-01-16'),
        ('Teclado Mecanico', 'Eletronicos', 5, 300.00, '2026-01-17'),
        ('Cadeira Office', 'Mobiliario', 3, 800.00, '2026-01-18'),
        ('Monitor 4K', 'Eletronicos', 4, 2000.00, '2026-01-19'),
        ('Mesa Ajustavel', 'Mobiliario', 2, 1200.00, '2026-01-20'),
        ('Headset RGB', 'Eletronicos', 8, 250.00, '2026-01-21'),
        ('Webcam HD', 'Eletronicos', 6, 180.00, '2026-01-22'),
        ('Luminaria LED', 'Mobiliario', 15, 90.00, '2026-01-23'),
        ('Suporte Laptop', 'Acessorios', 20, 60.00, '2026-01-24')
    ])
    conexao.commit()  # Salva as alterações! Sem isso, os dados não ficam gravados.
"""
Questão 1 (Básico): Liste todos os produtos da categoria "Eletronicos" ordenados pelo preço unitário do maior para o menor.
"""
"""
cursor.execute("SELECT produto, categoria, quantidade, preco_unitario FROM vendas  WHERE categoria = 'Eletronicos'  ORDER BY preco_unitario DESC")
for row in cursor.fetchall():
    print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
"""
#Questão 2 (Intermediário - Agregação): Calcule o valor total faturado por categoria. (Dica: Valor Total = Quantidade * Preço Unitário). Ordene pelo maior faturamento.
#RESPOSTA:
"""
cursor.execute("SELECT categoria,SUM(quantidade * preco_unitario) AS faturamento_total from vendas  Group By categoria  ")
for row in cursor.fetchall():
    print(f"{row[0]} | {row[1]}")
"""


"""""
Questão 3 (Intermediário - Filtro + Group By): Quais categorias venderam mais de 20 unidades no total? Mostre apenas o nome da categoria e a soma das quantidades.
R:
cursor.execute("SELECT categoria,SUM(quantidade) AS venderam_mais from vendas  Group By categoria Having venderam_mais > 20 ")
for row in cursor.fetchall():
    print(f"{row[0]} | {row[1]}")
"""

"""
4)por uma desafio intermediário que usa apenas o que você já sabe (JOIN mental com subconsulta simples ou CASE WHEN):Questão 4 (Substituta - Intermediário com CASE WHEN):
Crie uma consulta que classifique as categorias em três faixas de faturamento e mostre o total de unidades vendidas por categoria.
Regras da classificação:
Total vendido ≥ 40 unidades: 'Alto Volume'
Total vendido entre 21 e 39 unidades: 'Volume Médio'
Total vendido ≤ 20 unidades: 'Baixo Volume'
Requisitos:

Selecione categoria.
Calcule SUM(quantidade) como total_unidades.
Crie a coluna faixa_volume usando CASE WHEN.
"""
cursor.execute("""SELECT categoria,SUM(quantidade) AS total_unidades,
               CASE
                   WHEN SUM(quantidade)  >= 40 THEN 'Alto Volume'
                   WHEN SUM(quantidade) >= 21 AND  SUM(quantidade) <= 39 THEN 'Volume Médio'
                   ELSE'Baixo Volume'
               END AS faixa_volume
            FROM vendas
            GROUP BY categoria 
            ORDER BY total_unidades DESC
               """)
for row in cursor.fetchall():
    print(f"{row[0]} | {row[1]} | {row[2]}")


# 4. Fecha SÓ no final, quando terminar tudo
cursor.close()
conexao.close()