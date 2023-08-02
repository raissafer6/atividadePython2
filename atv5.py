def numeros_pares(lista):
    # Usando list comprehension para criar uma nova lista com apenas os números pares
    numeros_pares = [numero for numero in lista if numero % 2 == 0]
    return numeros_pares

lista_de_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = numeros_pares(lista_de_numeros)
print(resultado)
