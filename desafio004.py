#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
#Para este código utilizei alguns métodos para verificar se possui as seguintes características:

thing = input('Digite algo: ')

#Primeiro solicitando a entrada do usuário


print(f"{thing} é um ", type(thing))
#Este primeiro método sempre vai retornar "str", pois na declaração da variável "thing" eu não declarei o seu tipo

print("Só tem espaços?", thing.isspace())
print("É um número?", thing.isnumeric())
print("É alfabético? ", thing.isalpha())
print("É alfanumérico? ", thing.isalnum())
print("Está em maiúscula? ", thing.isupper())
print("Está em minúscula?", thing.islower())
print("Está capitalizada", thing.istitle())

#Este código poderia ser melhorado adicionando condições, como o exemplo abaixo:

if thing.isnumeric() == True:
    print(f"{thing} contém apenas números.")
else:
    print(f"{thing} não contém apenas números.")