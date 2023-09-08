#Desenvolver um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
#Existem duas maneiras principais de realizar este desafio. O primeiro, coforme abaixo é declarando variáveis com o resultado da média ou realizando direto na sintaxe f string
#A segunda opção ficaria menos organizada
name = str(input('Qual o nome do aluno(a)? '))
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1+n2)/2
print(f'A media de {name} é {m}') #primeira opção
print(f'A média de {name} é {(n1+n2)/2}') #segunda opção