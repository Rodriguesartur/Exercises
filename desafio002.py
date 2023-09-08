#Neste desafio será necessário criar uma interação com usuário, solicitando o seu nome e em seguida apresentar o nome digitado seguido da mensagem "É um prazer te conhecer, (Nome)!"
#Neste primeiro momento vou solicitar a entrada do usuário pedindo seu nome.

name = input(str("Digite seu nome: "))

#Em seguida, vou utilizar a função print para apresentar a mensagem armazenada na variavel name, que será inserida no meio do restante da mensagem apresentada através da formatação abreviada "f"

print(f"É um prazer te conhecer, {name}!")
