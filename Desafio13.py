# Imprime o título do desafio
print('====== DESAFIO 13  ======')

# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário, com 15% de aumento.

# Solicite o valor do salário do usuário
salario = float( input('Informe seu salário: R$ '))

# Calcula o valor do aumento
# pode ser usuádo salario + (salario * 15 / 100)
aumento = salario * 0.15

# Calcula o novo salário com o aumento
salarioComAumento = salario + aumento

# Exibe o novo salário e o valor do aumento
print('Parabéns, seu novo salário é de: R$ {:.2f}'.format(salarioComAumento))
print('Valor do aumento (15%): R${:.2f}'.format(aumento))

print(f'Valor do aumento (15%): R${aumento:.2f}')