def encontrar_maior_menor_palavra(lista_palavras):
    if not lista_palavras:
        return None, None

    menor_palavra = lista_palavras[0]
    maior_palavra = lista_palavras[0]

    for palavra in lista_palavras:
        if len(palavra) < len(menor_palavra):
            menor_palavra = palavra
        if len(palavra) > len(maior_palavra):
            maior_palavra = palavra

    return menor_palavra, maior_palavra

if __name__ == "__main__":
    # Obtém a lista de palavras do usuário
    lista_palavras = input("Digite as palavras separadas por espaço: ").split()

    # Encontra a maior e a menor palavra
    menor, maior = encontrar_maior_menor_palavra(lista_palavras)

    # Exibe os resultados
    if menor and maior:
        print(f"A menor palavra é: {menor}")
        print(f"A maior palavra é: {maior}")
    else:
        print("A lista de palavras está vazia.")
