# Imprime o título do desafio
print('====== DESAFIO 19 ======')

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

# Importamos a biblioteca random

# Dica: também podemos importar somente a função que precisamos da biblioteca random
# from random import choice \\ No nome_sorteado seria = nome_sorteado = choice(nomes)
import random

# Solicita ao usuário que digite os 4 nomes de alunos
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

# Lista com os nomes
nomes = [n1, n2, n3, n3]

# random.choice para sortear um dos nomes da lista.
nome_sorteado = random.choice(nomes)

# Exibição
print(f'O nome escolhido aleatoriamente foi: {nome_sorteado}!!')