#3. Diferença de Conjuntos:
#Crie um conjunto com os livros que você já leu e outro com os livros que você deseja ler.
#Encontre os livros que você ainda não leu e imprima a lista.
livros_lidos = {"Dom Casmurro", "O Triste Fim de Policarpo Quaresma", "A Hora da Estrela"}
livros_desejo = {"Cem Anos de Solidão", "1984", "O Senhor dos Anéis"}

diferenca = livros_desejo - livros_lidos

print(f"Livros que ainda não li: {diferenca}")
