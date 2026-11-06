import csv
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\que_sou_eu.txt'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor) 
    for linha in leitor:
        print(linha)