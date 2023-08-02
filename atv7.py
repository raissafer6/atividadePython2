def fatorial(numero):
    if numero < 0:
        raise ValueError("O número deve ser não negativo.")
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Exemplos de uso:
print(fatorial(5))   # 120 (5! = 5 * 4 * 3 * 2 * 1 = 120)
print(fatorial(0))   # por convenção, 0! é definido como 1)
print(fatorial(10))  # (10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800)
