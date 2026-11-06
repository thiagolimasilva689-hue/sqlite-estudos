import csv
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\teste.txt'
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # pula o cabeçalho
    for linha in leitor:
        print(linha)