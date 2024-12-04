# Imprime o título do desafio
print('\n====== DESAFIO 18 ======\n')

#Faça um programa que leia um angulo qualquar a mostra na
#tala o valor do seno, cosseno a tangente desse angulo.

# Importamos apenas as funções necessárias da biblioteca math.
from math import sin, cos, tan, radians

# Entrada do usuário:
angulo = float(input('Digite o valor em graus: '))

# A função radians() converte o ângulo de graus para radianos.
angulo_radiano = radians(angulo)

# Cálculo das funções trigonométricas:
s = sin(angulo_radiano)
c = cos(angulo_radiano)
t = tan(angulo_radiano)

# Exibição
print(f'O ângulo de {angulo}º tem: ')
print(f'O seno: {s:.2f}')
print(f'O Cansseno: {c:.2f}')
print(f'A Tangente: {t:.2f}')

# Código mais fácil
# import math
# angulo = float(input('Digite o ângulo que você sejesa: ')
# seno = math.sin(math.radians (angulo))
# print(f'O ângulo de {angulo:.2f} tem os SENO de {seno:.2f}')
# cosseno = math.cos(math.radians(angulo))
# print(f'O ângulo de {angulo:.2f} tem os COSSENO de {cosseno:.2f}')
# tangente = math.tan(math.radians(angulo))
# print(f'O ângulo de {angulo:.2f} tem os TANGENTE de {tangente:.2f}')