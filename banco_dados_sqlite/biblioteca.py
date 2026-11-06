import csv
import sqlite3

# Conectar ao banco
conexao = sqlite3.connect('biblioteca.db')
cursor = conexao.cursor()

# Criar tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros  (
        titulo  TEXT,
        autor  TEXT,
        ano  INTEGER,
        paginas INTEGER        
    )
''')
# LER O CSV
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\livros.csv'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # Pular cabeçalho

    for linha in leitor:
        cursor.execute("INSERT INTO livros VALUES (?, ?, ?, ?)", 
                   (linha[0], linha[1], int(linha[2]), int(linha[3])))
#CONSULTAS
"""
1)
Peça ao usuário um autor

Mostre todos os livros desse autor
"""
# fazer um input
#autor_usuario = input("Digite o nome desse autor: ")
#cursor.execute('SELECT * FROM livros WHERE autor = ?', (autor_usuario,))
#for linha in cursor.fetchall():
 #   print(linha)

"""
2)
Atualize o número de páginas de "1984" para 350 

Exclua "O Pequeno Príncipe" 

Mostre a tabela atualizada 
"""
# atualizar
#cursor.execute('''
 #              UPDATE livros
  #             set paginas = 350
   #            where '1984'
        #       ''')  
#conexao.commit()  
# excluir
#cursor.execute('''
   # DELETE FROM livros
   # WHERE titulo = 'O Pequeno Príncipe'
#''')
#conexao.commit()

# Mostrar tabela atualizada
#cursor.execute('SELECT * FROM livros')
#for linha in cursor.fetchall():
 #   print(linha)

"""
 Etapa 5 — Relatório final 

Mostre: 

Quantos livros no total 

Livro mais antigo (título e ano) 

Livro mais novo (título e ano) 

Média de páginas 
 """
# contar
#cursor.execute('SELECT COUNT(*) FROM livros')
#total = cursor.fetchone()[0]
#print(f"Total de livros: {total}")

#Livro mais antigo (título e ano) 
#resultado = cursor.execute('''SELECT  
 #              titulo,
  #             ano
   # FROM livros
    #ORDER BY ano asc
     #LIMIT 1''')
#resultado = cursor.fetchone()
#print(f"Mais antigo: {resultado[0]} ({resultado[1]})")

#Média de páginas 
resultado = cursor.execute('SELECT AVG(paginas) FROM livros')
resultado = cursor.fetchone()
#print(f"A media de paginas é : {resultado[0]:.2f}")


     
    

