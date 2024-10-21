# Imprime o título do desafio
print('====== DESAFIO 08  ======')

# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

# Solicita ao usuário que insira um valor em metros
metros = float( input('Insira a Metragem: '))

# Converte o valor de metros para centímetros (1 metro = 100 centímetros)
centimentos = metros * 100

# Converte o valor de metros para milímetros (1 metro = 1000 milímetros)
milimetros = metros * 1000

# Exibe os valores convertidos
print('Valor em Metros: {} Valor em Centimetros: {} Valor em Milímetros: {}'.format(metros, centimentos, milimetros))