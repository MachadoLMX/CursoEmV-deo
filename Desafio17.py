# Imprime o título do desafio
print('====== DESAFIO 17  ======')

# Faça um programa que leia o comprimento do cateto oposto e adjacente
# de um triangulo, calcule e mostre o comprimento da hipotenusa

# Importa a função sqrt da biblioteca math
from math import sqrt

# Entrada dos catetos
o = float( input('Digite o cateto oposto: '))
a = float( input('Digite o cateto adjacente: '))

# Calcula a hipotenusa
h = sqrt(o**2 + a**2)

# Exibe o resultado
print(f'O valor do cateto oposto {o} e cateto adjascente {a}, a hipotenusa do triangulo vai medir {h:.2f}')

# Calculo mais fácil

# import math
# co = float( input('Comprimento do cateto oposto: '))
# ca = float( input('Comprimento do cateto adjacente: '))
# hi = math.hypot(co, ca)
# print(f'A hipotenusa vai medir {hi:.2f}')