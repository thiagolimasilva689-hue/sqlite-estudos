

"""
Parte 1: Criar banco SQLite 

Crie um banco estudos.db com tabela materias: 

nome, horas_estudadas, dificuldade (1-5), status (Pendente/Concluído) 
"""
import sqlite3

# Conectar ao banco
conexao = sqlite3.connect('estudos.db')
cursor = conexao.cursor()

#criar tabelas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS materias  (
        nome  TEXT,
        horas_estudada INT,
        nivel_dificuldade INT,
        status TEXT
        
    )
''')
#Parte 2: Inserir dados 

#Insira 8 matérias com dados realistas. 

cursor.execute("INSERT INTO materias VALUES ('Python', 40, 2, 'Concluído')")
cursor.execute("INSERT INTO materias VALUES ('SQL', 30, 1, 'Concluído')")
cursor.execute("INSERT INTO materias VALUES ('Excel', 15, 1, 'Concluído')")
cursor.execute("INSERT INTO materias VALUES ('Matemática Discreta', 20, 5, 'Pendente')")
cursor.execute("INSERT INTO materias VALUES ('Algoritmos', 50, 4, 'Pendente')")
cursor.execute("INSERT INTO materias VALUES ('Inglês', 25, 3, 'Pendente')")
cursor.execute("INSERT INTO materias VALUES ('Power BI', 10, 2, 'Pendente')")
cursor.execute("INSERT INTO materias VALUES ('Pandas', 8, 2, 'Pendente')")
conexao.commit()


"""
"""


#Parte 3: Consultas 



#Total de horas estudadas 
cursor.execute('''SELECT SUM(horas_estudada) from materias ''')
horas = cursor.fetchone()
print(f" O TOTAL DE HORAS NO CURSO : {horas[0]}")

#Média de dificuldade 
cursor.execute('SELECT AVG(nivel_dificuldade) FROM  materias')
media = cursor.fetchone()
print(f"A MEDIA DE DIFICULDADE DO CURSO: {media[0]}")

#Matérias concluídas vs pendentes 
# concluídas
cursor.execute('''SELECT COUNT(*) FROM materias WHERE status = 'Concluído' ''')
aprovados = cursor.fetchone()
print(f"QUANTOS FORAM APROVADOS NO CURSO: {aprovados[0]}")

#pendentes
cursor.execute('''SELECT COUNT(*) FROM materias WHERE status = 'Pendente' ''')
reprovador = cursor.fetchone()
print(f"QUANTOS FORAM REPROVADOS NO CURSO: {reprovador[0]}")

#Matéria mais difícil 
cursor.execute('''SELECT nome, nivel_dificuldade
FROM materias
ORDER BY nivel_dificuldade DESC
LIMIT 1''')
difil = cursor.fetchone()
print(f"A MATERIA MAIS DIFICIL DO CURSO : {difil[0]}")



