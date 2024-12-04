# Imprime o título do desafio
print('====== DESAFIO 16  ======')

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

# Importamos a biblioteca math para usar a função math.trunc, que retorna a parte inteira de um número
# Dica: Para importar somente a função trunc, pode-se usar 'from math import trunc' em vez de importar a biblioteca inteira
import math

# Solicita ao usuário que digite um número real (com casas decimais)
num = float(input('Digite um número: '))

# Utiliza a função math.trunc para obter a parte inteira do número fornecido pelo usuário
inteiro = math.trunc(num)

# Exibe o número digitado e a sua parte inteira, formatando a mensagem com f-strings
print (f'O número digitado é {num} e o número inteiro é {inteiro}')