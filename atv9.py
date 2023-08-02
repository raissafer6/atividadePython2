#Crie uma função que receba uma lista de strings e retorne uma nova lista 
#com todas as palavras em letras maiúsculas.]

def palavras_maiusculas(lista_strings):
    maiusculas = [palavra.upper() for palavra in lista_strings]
    return maiusculas

lista_strings = ["Python", "é", "uma", "linguagem", "de", "programação"]
resultado = palavras_maiusculas(lista_strings)
print(resultado)  
