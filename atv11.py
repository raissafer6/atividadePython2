import random

def jogo_adivinhacao():
    numsecreto = random.randint(1, 100)
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")

    while True:
        tentativa = int(input("Digite sua tentativa: "))
        tentativas += 1

        if tentativa == numsecreto:
            print(f"Parabéns! Você acertou o número {numsecreto} em {tentativas} tentativas.")
            break
        elif tentativa < numsecreto:
            print("Tente novamente! O número secreto é maior.")
        else:
            print("Tente novamente! O número secreto é menor.")

# Executar o jogo
jogo_adivinhacao()
