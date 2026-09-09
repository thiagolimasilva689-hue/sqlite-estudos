import sqlite3
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

cursor.execute('''
         Create Table IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                curso TEXT
                               )
''')
alunos = [
    ('Thiago Lima', 20, 'Sistemas de Informação'),
    ('Ana Souza', 22, 'Ciência de Dados'),
    ('João Pedro', 19, 'Engenharia de Software'),
    ('Maria Clara', 21, 'Sistemas de Informação'),
    ('Lucas Alves', 23, 'Ciência de Dados')
]

cursor.executemany('''
    INSERT INTO alunos (nome, idade, curso) VALUES (?, ?, ?)
''', alunos)




cursor.execute('''
         Create Table IF NOT EXISTS notas (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                aluno_id	INTEGER,
                nota	REAL
                               )
''')

notas = [
    (1,8.5),
    (1,7.8),
    (1,6.5),
    (2,8.9),
    (2,7.5),
    (2,7.4),
    (3,5.5),
    (3,6.7),
    (3,9.7),
    (4,4.9),
    (4,7.4),
    (5,5.2),
    (5,6.8),
    (5,7.8),
    (4,6.5),
    (5,7.9)
]
cursor.executemany('''
    INSERT INTO notas (aluno_id,nota) VALUES (?, ?)
''', notas)


#QUERYS
"""
Questão 1 — Todos os alunos
Traga todos os campos de todos os alunos da tabela alunos.

R:
 
"""
cursor.execute('SELECT * FROM alunos')
for id,nome,idade,curso in cursor.fetchall():
        print(f" {id}| {nome} | {idade} | {curso}")

"""
Questão 2 — Alunos de Sistemas de Informação
Traga o nome e a idade dos alunos que fazem Sistemas de Informação.

sql
SELECT nome, idade 
FROM alunos 
WHERE curso = 'Sistemas de Informação';
R:
  
"""
cursor.execute('''SELECT nome, idade 
FROM alunos "Sistemas de Informação " ''')
for   nome,idade in cursor.fetchall():
     print(f" {nome} | {idade} ")

"""
Questão 3 — Média de notas por aluno
Mostre o nome do aluno e a média das notas dele, ordenado da maior média para a menor.

   
"""

cursor.execute('''
         SELECT 
               alunos.nome as Nome,
               AVG(notas.nota) as Media_Nota
        from notas
                 join alunos
                           on alunos.id = notas.aluno_id
                group by alunos.nome
                ORDER BY AVG(notas.nota) DESC
''')
for   nome,nota in cursor.fetchall():
     print(f" {nome} | {nota:.2f} ")     
"""
Questão 4 — Aluno com a maior nota
Mostre o nome do aluno e a nota mais alta que ele tirou, apenas do aluno com a maior nota.


"""
cursor.execute('''
         SELECT 
               alunos.nome as Nome,
               MAX(notas.nota) as MAIOR_Nota
        from notas
                 join alunos
                           on alunos.id = notas.aluno_id
                group by alunos.nome
''')
Nerd = cursor.fetchone()
print(f"QUE É MAIOR NERD DA SALA É : { Nerd[0] }")

"""Questão 5 — Alunos com média maior que 7
Mostre o nome do aluno e a média dele, apenas para alunos com média maior que 7."""
cursor.execute('''
         SELECT 
               alunos.nome as Nome,
               AVG(notas.nota) as Media_Nota
        from notas
                 join alunos
                           on alunos.id = notas.aluno_id
                group by alunos.nome
                HAVING notas.nota > AVG(notas.nota)
''')
for   nome,nota in cursor.fetchall():
     print(f" {nome} | {nota:.2f} ")   


