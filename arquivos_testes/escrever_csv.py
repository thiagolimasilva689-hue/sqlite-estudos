
#criar arquivos
import csv
caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\csv\pessoas.csv'
with open(caminho, 'w', newline='', encoding='utf-8') as arquivo:
       escritor = csv.writer(arquivo)
       escritor.writerow(['nome', 'idade', 'cidade','Estado'])
       escritor.writerow(['Thiago', '19', 'Coxim',"MS"])
       escritor.writerow(['silva', '48', 'Chopinzinho',"PR"])
       escritor.writerow(['Paulo', '58', 'Rio-Vende',"MS"])
       escritor.writerow(['Arthur', '17', 'São-Carlos',"SP"])
print("Arquivo criado com sucesso!")
# Ler o arquivo(separado)
with open(caminho, 'r', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo)
    next(leitor)  # pula cabeçalho
    for linha in leitor:
        print(linha)


        