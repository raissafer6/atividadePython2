#Crie uma função que receba uma lista de números como argumento e retorne a média dos valores.

def calcular_media(lista):
    if not lista:
        return 0.0

    soma = sum(lista) 
    media = soma / len(lista) 
    return media

numeros = [1, 2, 3, 4, 5]
media_resultado = calcular_media(numeros)
print(f"A média dos números é: {media_resultado}")
