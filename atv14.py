def ordenar_lista(lista):
    return sorted(lista)

# Exemplo de uso:
numeros = [5, 2, 9, 1, 7, 3]
lista_ordenada = ordenar_lista(numeros)
print(lista_ordenada)  # Output: [1, 2, 3, 5, 7, 9]


def ordenar_lista_inplace(lista):
    lista.sort()

# Exemplo de uso:
numeros = [5, 2, 9, 1, 7, 3]
ordenar_lista_inplace(numeros)
print(numeros)  # Output: [1, 2, 3, 5, 7, 9]
