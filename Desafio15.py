# Imprime o título do desafio
print('====== DESAFIO 15  ======')

# Esqueva um programa que pergunta a quantidade de km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

dias = int (input ('Quantos dias alugados? '))
km = float (input('Quantos Km rodados? '))

pago = (dias * 60) + (km * 0.15)

print ('O total de dias a pagar é de R${:.2f}'.format(pago))

