'''Fazer um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.'''
#Coletando os dados do produto
product = str(input('Qual o produto que você deseja aplicar o desconto?'))
price = float(input('Informe o valor do produto R$ '))
#Aplicando o desconto e armazenando numa nova variável
new_price = price-price*0.05
print(f'Com o desconto no(a) {product}, o valor passa a ser R$ {new_price:.2f}.')