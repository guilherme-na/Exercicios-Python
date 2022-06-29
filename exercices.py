 //Exercicio 01 (If e Else,print)

print("************************************")
print("Bem Vindo ao Jogo de Adivinhação! :)")
print("************************************")

num_secreto = 42
chute = input("Digite o seu numero:" )

print("Você digitou:", chute)

if (num_secreto == chute):
    print("Você Acertou!!")
else:
    print("Você errou!")
    print("Fim de Jogo!")



