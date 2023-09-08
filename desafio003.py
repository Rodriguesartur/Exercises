#Neste desafio devo criar um programa que lerá dois números inteiros e mostrará a soma entre eles.
#Primeiramente vou criar duas variáveis para solicitar ao usuário e armazenar os números que serão somados

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))

#Em seguida, vou criar uma nova variável para armazenar a soma dos valores e apresentá-los através da função print e com a formatação f
sum = n1+n2
print(f'A soma dos valores é igual a {sum}')
