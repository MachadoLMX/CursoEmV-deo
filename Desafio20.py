# Imprime o título do desafio
print('====== DESAFIO 20 ======')

# O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."

# Importamos a biblioteca random

# Dica: também podemos importar somente a função que precisamos da biblioteca random
# from random import shuffle \\ No random.shuffle(nomes) seria shuffle.nomes
import random

# Solicita ao usuário que digite os 4 nomes de alunos
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))

# Lista com os nomes
nomes = [n1, n2, n3, n4]

# random.choice para sortear um dos nomes da lista.
random.shuffle(nomes)

# Exibição
print(f'A ordem escolhida aleatoriamente da apresentação foi: {nomes}!!')