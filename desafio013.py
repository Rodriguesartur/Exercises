'''Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.'''
#Coletando dados
name = str(input('Digite o nome do funcionário: '))
salary = float(input(f'Digite o salário atual de {name}: '))

#Realizando cálculos e armazenando em uma nova variável
new_salary = salary+(salary*15/100)
print(f'O novo salário de {name} é de R$ {new_salary:.2f}.')
