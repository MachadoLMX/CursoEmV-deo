# Imprime o título do desafio
print('====== DESAFIO 11  ======')

# Faça um programa que leia a largura e a altura de uma parede em metros,
# Calcule a sua área e a quantidade de tinta necessária para pinta-la,
# Sabendo que cada litro de tinta pinta uma área de 2m².

# Solicita ao usuário a largura da parede em metros
largura = float( input('Informe a largura da parede: '))

# Solicita ao usuário a altura da parede em metros
altura = float( input('informe a altura da parede: '))

# Calcula a área da parede
area = largura * altura

# Calcula a quantidade de tinta necessária (1 litro cobre 2 m²)
litroTinta = area / 2

print('A área de parede é = {}m²'.format(area))
print('Você precisará de {} litros de tinta para pintar a parede'.format(litroTinta))
