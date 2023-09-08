#Criar um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
#Como de costume inicio declarando uma variável e recebendo um valor do usuário
n = int(input('Informe um número: '))

#Em seguida, apresento o valor em tela com a sintaxe f string ja aplicando os operadores necessários para os resultados
print(f'Você informou o número {n}')
print(f'Seu dobro é {n*2}')

#Outra maneira de realizar seria armazenando os resultados em uma variável e apresentando também com a sintaxe f string
triple = n*3
square = n**0.5
print(f'Seu triplo vale {triple}')
print(f'E sua raiz quadrada é {square}')