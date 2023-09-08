#Escrever um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#Solicito entrada do usuário em "float" já que a medida pode ser um número real
m = float(input("Digite o valor em metros: "))
cm = m * 100
mm = m * 1000

#Após isso é só apresentar o resultado
print(f'Você digitou {m}m')
print(f'Este valor equivale a {cm}cm e {mm}mm')

