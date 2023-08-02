def is_palindrome(word):
    # Remover espaços em branco e converter para letras minúsculas para ignorar diferenças de maiúsculas/minúsculas
    word = word.replace(" ", "").lower()
    
    # Verificar se a palavra é igual à sua forma invertida
    return word == word[::-1]

# Exemplos de uso:
print(is_palindrome("uva")) 
print(is_palindrome("osso")) 
print(is_palindrome("ovo"))    
