# Imprime o título do desafio
print('====== DESAFIO 06  ======')

# Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

num = int (input('Insira um valor: '))

dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('Seu número é = {}, Seu dobro é = {}, Seu triplo é = {}, Sua Raiz Quadrada é = {:3f}'.format(num, dobro, triplo, raiz))