import sqlite3
import csv
# Conectar ao banco
conexao = sqlite3.connect('minha_lista_compras.db')
cursor = conexao.cursor()

#criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS gas_vendas  (
       data TEXT,
       Endereco text,
       Quantidade INT,
       Preco_Unitario FLOAT,
       Tipo_Venda TEXT,
       Forma_Pagamento TEXT
    )
''')
# LER O CSV
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\vendas_gas_07.csv'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho
    for linha in leitor:
     if len(linha) == 6: # CONTAR SE NUMEROS DE LINHAS ESTÁ CORRETO
        cursor.execute("INSERT INTO gas_vendas VALUES (?, ?, ?, ?,?,?)",
                       (linha[0], linha[1], int(linha[2]), float(linha[3]),linha[4],linha[5]))
    conexao.commit()

"""
1 — Total de vendas por dia
Qual dia vendeu mais? Qual o faturamento diário?
"""
cursor.execute('''
SELECT data, SUM(Quantidade * Preco_Unitario) AS faturamento
FROM gas_vendas
GROUP BY data
''')
for data,total in cursor.fetchall():
    print(f"{data}: R$ {total:.2f}")

"""
2 — Total de vendas por forma de pagamento
PIX, Cartão, Crédito, Dinheiro, Fiado — qual é mais usado?
"""
cursor.execute('''
SELECT Forma_Pagamento, COUNT(*) AS total
FROM gas_vendas
GROUP BY Forma_Pagamento
ORDER BY total DESC
''')
pagar_mais = cursor.fetchone()
print(f"A FORMA DE PAGAMENTO MAIS USADO É  { pagar_mais[0] }")

"""
3 — Total de vendas por endereço
Quais clientes compraram mais? (só 1 unidade cada, mas pode agrupar)
"""
cursor.execute('''
SELECT Endereco , COUNT(*) as vezes
FROM gas_vendas
GROUP BY Endereco
ORDER BY vezes DESC
''')
cliente = cursor.fetchone()
print(f"que mais pediu foi  { cliente[0] }")

"""
5 — Média de preço unitário
Qual o preço médio do botijão? (variou entre 130 e 135)
"""
cursor.execute('''
SELECT AVG(Preco_Unitario) as media from gas_vendas
''')
media = cursor.fetchone()
print(f" MEDIA DE VALOR DOS GÁS É  { media[0] }")

"""
6 — Vendas fiado vs à vista
Quantas vendas foram fiado? Quantas à vista?
"""
# Fiado
cursor.execute('''SELECT COUNT(*) FROM gas_vendas WHERE Tipo_Venda = 'Fiado' ''')
fiado = cursor.fetchone()
print(f"Fiado: {fiado[0]}")

# À Vista
cursor.execute('''SELECT COUNT(*) FROM gas_vendas WHERE Tipo_Venda = 'À Vista' ''')
vista = cursor.fetchone()
print(f"À Vista: {vista[0]}")

"""
7 — Clientes que pagaram com PIX

Liste todos os clientes que usaram PIX.

"""
cursor.execute('''
    SELECT Endereco, Forma_Pagamento
    FROM gas_vendas
    WHERE Forma_Pagamento = 'PIX'
''')
for cliente, pagamento in cursor.fetchall():
    print(f"Cliente: {cliente} | Pagamento: {pagamento}")

"""
8 — Clientes que pagaram fiado
Quem comprou fiado? (depois precisa cobrar!)
"""
cursor.execute('''
    SELECT Endereco, Forma_Pagamento
    FROM gas_vendas
    WHERE Forma_Pagamento = 'Fiado'
    limit 1
''')
for cliente, pagamento in cursor.fetchall():
    print(f"Cliente: {cliente} | Pagamento: {pagamento}")

  
