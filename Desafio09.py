# Imprime o título do desafio
print('====== DESAFIO 09  ======')

# Este programa solicita um número inteiro ao usuário e exibe a sua tabuada de 1 a 10

# Solicita ao usuário um número inteiro
num = int( input('Insira um número inteiro: '))

# Exibe o título da tabuada para o número informado
print ('Tabuada do núemro: {}'. format(num))

# Exibe a tabuada do número de 1 a 10, usando o format() para organizar a saída
print('{}*1 = {}'.format(num, num*1))
print('{}*2 = {}'.format(num, num*2))
print('{}*3 = {}'.format(num, num*3))
print('{}*4 = {}'.format(num, num*4))
print('{}*5 = {}'.format(num, num*5))
print('{}*6 = {}'.format(num, num*6))
print('{}*7 = {}'.format(num, num*7))
print('{}*8 = {}'.format(num, num*8))
print('{}*9 = {}'.format(num, num*9))
print('{}*10 = {}'.format(num, num*10))
