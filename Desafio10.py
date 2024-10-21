# Imprime o título do desafio
print('====== DESAFIO 10  ======')

# Façã um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar
# Considere US$1,00 = R$3,27

# Define a cotação do dólar
cotacao_dolar = 3.27

# Solicita ao usuário quanto dinheiro ele tem na carteira em Reais
reais = float( input('Informe quanto dinheiro em Reais você tem na carteira: '))

# Calcula quantos dólares podem ser comprados
dolares = reais / cotacao_dolar

# Exibe o resultado formatado, mostrando quanto em Reais e quantos dólares podem ser comprados
print('Com R$: {}, você pode comprar US${:.2f}.'.format(reais, dolares))
