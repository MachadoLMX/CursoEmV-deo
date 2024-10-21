# Imprime o título do desafio
print('====== DESAFIO 07  ======')

# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float (input('Insira a primeira Nota: '))
nota2 = float (input('Insira a segunda Nota: '))

# Calcula a média das duas notas
media = (nota1 + nota2) / 2

# Exibe as notas e a média final
print ('Primeira nota: {} Segunda nota: {} Média Final: {}'.format(nota1, nota2, media))

# Verifica se a média é suficiente para aprovação (nota maior ou igual a 7)
if media >= 7:
    print('Aprovado!!! sua média é: ', media)
else:
    print('Reprovado!!! Sua média é: ', media)