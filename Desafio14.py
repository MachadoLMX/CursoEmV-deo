# Imprime o título do desafio
print('====== DESAFIO 14  ======')

# Escreva um programa que converta uma temperatura digitada ºC e converta para ºF

c = float(input ('Qual a temperatura em ºC: '))

f = (c * 1.8) + 32

print('A temperatura de {}ºC corresponde a {}ºF!'.format(c,f))