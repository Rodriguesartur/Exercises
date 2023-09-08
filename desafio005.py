#Fazer um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
#Para resoluçao deste desafio, primeiro irei declarar uma variável com uma entrada para o usuário informar o valor que será utilizado

value = int(input('Informe um valor: '))

#Após isso, irei utilizar a função "print" para apresentar na tela o retorno do valor com a resolução do desafio

print(f'Você informou o valor {value}. O seu sucessor é {value+1}, e o seu antecessor é {value-1}.')