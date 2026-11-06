"""
fetchone() — Quando o resultado é 1 linha só
Exemplo	Por que
COUNT(*)	Retorna um número
AVG(coluna)	Retorna um número
MAX(coluna)	Retorna um número
MIN(coluna)	Retorna um número
SELECT ... WHERE id = ?

cursor.execute('SELECT COUNT(*) FROM animais')
total = cursor.fetchone()[0]

fetchall() — Quando o resultado pode ter várias linhas
Exemplo	Por que
SELECT * FROM animais	Vários animais
SELECT * WHERE idade > 10	Pode ter vários
SELECT * ORDER BY nome

cursor.execute('SELECT * FROM animais')
for linha in cursor.fetchall():
    print(linha)
"""
"""
Regra simples e direta.

Quando usar GROUP BY
Sempre que você quiser agrupar dados por alguma categoria.

Exemplos práticos
Pergunta	GROUP BY
Quantos clientes por loja?	GROUP BY store_id
Total de vendas por produto?	GROUP BY produto
Média de notas por turma?	GROUP BY turma
Quantos filmes por classificação?	GROUP BY rating
Regra de ouro
A coluna que você coloca no GROUP BY é a mesma que você quer "por".

sql
-- "Quantos clientes POR LOJA?"
SELECT store_id, COUNT(*) 
FROM customer 
GROUP BY store_id;   -- ← agrupa POR LOJA
Como saber qual coluna agrupar
Pergunta	Agrupar por
"...por loja?"	store_id
"...por produto?"	produto
"...por cidade?"	cidade
"...por categoria?"	categoria
A palavra "por" entrega a coluna do GROUP BY.

Resumo
Situação	Usar
"Quantos ___ por ___?"	GROUP BY a segunda coluna
"Total de ___ por ___?"	GROUP BY a segunda coluna
Só contar/somar tudo (sem "por")	Não usa GROUP BY
"Agrupar por" = GROUP BY.

"""