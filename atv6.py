import random

def lancar_dado():
    # Simula o lançamento de um dado, retornando um número aleatório de 1 a 6
    return random.randint(1, 6)

def calcular_soma_dos_dados():
    # Lança os dois dados e retorna a soma dos valores obtidos
    dado1 = lancar_dado()
    dado2 = lancar_dado()
    return dado1 + dado2

if __name__ == "__main__":
    # Lança os dois dados e calcula a soma
    soma = calcular_soma_dos_dados()

    # Exibe o resultado
    print(f"O resultado do lançamento dos dados foi: {soma}")
