import pandas as pd

df = pd.read_csv(r'C:/Users/Thiago/OneDrive/Desktop/teiu/csv/livros.json')

df.to_excel('livros.xlsx')
print("ARQUIVANDO COM SUCESSO!")