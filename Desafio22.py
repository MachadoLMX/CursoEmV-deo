# Imprime o título do desafio
print('====== DESAFIO 22 ======')


# Entrada do nome
nome = str(input('Digite seu nome:')).strip()

# Exibe o nome em maiúsculas
print(f'Nome com as letras maiúsculas: {nome.upper()}\n')

# Exibe o nome em minúsculas
print(f'Nome com todas as letras minúsculas: {nome.lower()}\n')

# Conta quantas letras há no nome, sem contar os espaços
print(f'Quantas letras ao todo (sem considerar espaços): {len(nome)-nome.count(' ')}\n')

dividido = nome.split()
print(f'O primeiro nome tem: {len(dividido[0])} letras.')