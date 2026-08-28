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

conexao.commit()
print("ARQUIVANDO COM SUCESSO!")


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
print("ARQUIVANDO COM SUCESSO!")




