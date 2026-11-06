import csv
import sqlite3

# Conectar ao banco
conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()

# Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        nome TEXT,
        preco REAL,
        quantidade INTEGER
    )
''')

# Ler CSV e inserir no banco
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\produtos.txt'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho
    
    for linha in leitor:
        cursor.execute("INSERT INTO produtos VALUES (?, ?, ?)", 
                       (linha[0], float(linha[1]), int(linha[2])))

# Salvar
conexao.commit()

# Verificar se funcionou
cursor.execute("SELECT * FROM produtos")
for produto in cursor.fetchall():
    print(produto)

conexao.close()