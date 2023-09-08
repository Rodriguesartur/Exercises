#Criar um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Neste desafio será necessário criar 2 entradas para o usuário.
print('Bem vindo ao conversor de moedas automático by Artur!')

#A primeira para definir o "valor que a pessoa tem na carteira"
real = float(input('Digite o valor em Real (R$) que voce deseja converter em dólar (USD):'))

#A segunda para definir o valor "atual" do dólar
dolarhj = float(input('Qual o valor do Dólar hoje?'))

#Após isso, defino uma variável "usd" para receber o resultado da conversão e apresentá-lo ao usuário
usd = real/dolarhj
print(f'Com R$ {real:.2f} você pode comprar USD $ {usd:.2f}.')

'''Como o resultado pode ser um valor com muitas casas após a vírgula, utilizo da formatação da sintaxe f string ".2f"
para definir que o resultado terá no máximo duas casas após o ponto flutuante.'''


