# Imprime o título do desafio
print('====== DESAFIO 12  ======')

# Solicita ao usuário o preço do produto
precoProduto = float(input('Informe o preço do Produto: R$ '))

# Calcula o desconto de 5%
desconto = precoProduto * 0.05

# Calcula o preço final após o desconto
precoComDesconto = precoProduto - desconto

# Exibe o preço original e o preço final
print('Preço do produto era: R${}'.format(precoProduto))
print('Preço do produto agora com nosso desconto de 5% vai custar: R${:.2f}'.format(precoComDesconto))