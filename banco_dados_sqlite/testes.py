import sqlite3

conexao = sqlite3.connect('teste.db')
cursor = conexao.cursor()
"""


"""
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY,
    vendedor TEXT,
    produto TEXT,
    valor REAL,
    data_venda TEXT)
''')

cursor.execute('''
INSERT INTO vendas (id, vendedor, produto, valor, data_venda) VALUES
(1, 'Ana', 'Notebook', 3500.00, '2026-01-10'),
(2, 'Bruno', 'Mouse', 89.90, '2026-01-12'),
(3, 'Ana', 'Teclado', 199.90, '2026-01-15'),
(4, 'Carla', 'Monitor', 899.90, '2026-02-01'),
(5, 'Bruno', 'Notebook', 3500.00, '2026-02-03'),
(6, 'Ana', 'Mouse', 89.90, '2026-02-05'),
(7, 'Carla', 'Teclado', 199.90, '2026-02-10'),
(8, 'Bruno', 'Monitor', 899.90, '2026-02-12');
''')

#Qual o valor total de vendas?
cursor.execute('select sum(valor) from vendas')
total = cursor.fetchone()[0]
print(f"QUAL O VALOR DAS VENDAS É {total}")

#Quantas vendas cada vendedor fez?
cursor.execute('''
          select 
               count(*) as vendas,
               vendedor 
               from vendas
            group by vendedor
''')
for linha in cursor.fetchall():
    print(linha)


#Qual o valor total vendido por cada vendedor
cursor.execute('''
          select 
               sum(valor) as valor_vendass,
               vendedor 
               from vendas
            group by vendedor
''')
for linha in cursor.fetchall():
    print(linha)

#Qual foi a maior venda registrada?
cursor.execute('''
          select 
               max(valor) as maior_venda
               from vendas
''')
maior = cursor.fetchone()[0]
print(f"A MAIOR VENDA FOI : {maior}")

#Liste as vendas do mês de fevereiro, da maior para a menor.
cursor.execute('''
          SELECT valor, data_venda
          FROM vendas
          WHERE data_venda LIKE '2026-02%'
          ORDER BY valor DESC
''')
for linha in cursor.fetchall():
    print(linha)