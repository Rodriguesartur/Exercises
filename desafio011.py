'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''
#Primeiro coleto os dados necessários para realizar o cálculo da àrea²
l = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
m2 = l*h

#Após ter o valor da àrea em m², realizo a divisão por 2 para saber quantos litros de tinta serão necessários para pintar a parede
lt = float(m2/2)
print(f'A parede possui {l}m de largura e {h}m de altura.')
print(f'A area total desta parede é de {m2:.2f}m². Serão necessários {lt:.2f} litros de tinta para fazer a pintura.')

#Finalizando com o auxílio da sintaxe f string e limitando a duas casas decimais com ".2f".
