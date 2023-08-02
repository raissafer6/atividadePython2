def contar_palavras(texto):
    # Remover pontuações e converter para minúsculas
    texto = texto.lower()
    for char in '.,?!:;':
        texto = texto.replace(char, '')

    # Dividir o texto em palavras
    palavras = texto.split()

    # Criar um dicionário para armazenar a contagem de cada palavra
    contagem_palavras = {}

    # Contar as ocorrências de cada palavra
    for palavra in palavras:
        contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1

    return contagem_palavras

if __name__ == "__main__":
    # Obter o texto do usuário
    texto = input("Digite o texto: ")

    # Contar as ocorrências de cada palavra
    contagem = contar_palavras(texto)

    # Exibir o resultado
    for palavra, quantidade in contagem.items():
        print(f"A palavra '{palavra}' ocorre {quantidade} vezes no texto.")
