# Escreva o seu código aqui :-)
import random
import sys

print("Seja bem vindo ao jogo de adivinhação de números: ")
while True:

    choice_number = input("Digite o número teto do desafio: ").strip().upper()

    if choice_number.isdigit():
        choice_number = int(choice_number)
        break
    else:
        print("Erro: Valor informado não é um número. Favor informe um número!")


random_number = random.randint(0, choice_number)
n_choices = 0

while True:
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: Valor informado não é numérico. Favor informe um número!")
        continue

    n_choices += 1

    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("O número é menor que o número informado!")
    else:
        print("Chutou errado, o número é maior que isso!")

print("Número de tentativas: " + str(n_choices))

