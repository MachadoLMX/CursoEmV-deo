# Imprime o título do desafio
print('====== DESAFIO 04  ======')

# Este programa lê um valor do teclado e exibe seu tipo primitivo,
# além de diversas informações sobre o valor informado.

# A função input() captura a entrada do usuário
a = input('Digite algo: ')

# Exibe o tipo primitivo do valor informado
print('O tipo primitivo desse valor é', type(a))

# Exibe várias informações sobre o valor utilizando métodos de string
print('Só tem espaços?', a.isspace())            # Verifica se o valor contém apenas espaços
print('É um número?', a.isnumeric())             # Verifica se o valor é numérico
print('É alfabético?', a.isalpha())               # Verifica se o valor é alfabético
print('É alfanumérico?', a.isalnum())             # Verifica se o valor contém letras e números
print('Está em maiúsculas?', a.isupper())         # Verifica se todas as letras estão em maiúsculas
print('Está em minúsculas?', a.islower())         # Verifica se todas as letras estão em minúsculas
print('Está capitalizado?', a.istitle())          # Verifica se a primeira letra de cada palavra está em maiúscula
