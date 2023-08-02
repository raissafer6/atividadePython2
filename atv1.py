def soma_dois_numeros():
    numero1 = int(input("Digite o primeiro número (entre 1 e 100): "))
    numero2 = int(input("Digite o segundo número (entre 1 e 100): "))

    # Verifica se os números estão dentro do intervalo válido (1 a 100)
    if 1 <= numero1 <= 100 and 1 <= numero2 <= 100:
        resultado = numero1 + numero2
        print(f"A soma de {numero1} e {numero2} é: {resultado}")
    else:
        print("Por favor, digite números entre 1 e 100.")

# Chamando a função para executar o código
soma_dois_numeros()