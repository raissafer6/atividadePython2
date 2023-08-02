def encontrar_maior_menor_numero(sequencia_numeros):
    if not sequencia_numeros:
        return None, None

    menor_numero = sequencia_numeros[0]
    maior_numero = sequencia_numeros[0]

    for numero in sequencia_numeros:
        if numero < menor_numero:
            menor_numero = numero
        if numero > maior_numero:
            maior_numero = numero

    return menor_numero, maior_numero

if __name__ == "__main__":
    # Obtém a sequência de números do usuário
    sequencia_numeros = input("Digite a sequência de números separados por espaço: ").split()
    sequencia_numeros = [float(numero) for numero in sequencia_numeros]

    # Encontra o maior e o menor número
    menor, maior = encontrar_maior_menor_numero(sequencia_numeros)

    # Exibe os resultados
    if menor and maior:
        print(f"O menor número é: {menor}")
        print(f"O maior número é: {maior}")
    else:
        print("A sequência de números está vazia.")
