#Implemente um programa que converta uma temperatura em Celsius para 
#Fahrenheit ou vice-versa, de acordo com a escolha do usuário.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():

    escolha = int(input("Escolha uma opção (1 ou 2): "))
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")

    if escolha == 1:
        celsius = float(input("Digite a temperatura em Celsius: "))

        fahrenheit = celsius_para_fahrenheit(celsius)
        print(f"{celsius} graus Celsius é equivalente a {fahrenheit:.2f} graus Fahrenheit.")

    elif escolha == 2:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"{fahrenheit} graus Fahrenheit é equivalente a {celsius:.2f} graus Celsius.")

    else:
        print("Escolha inválida. Por favor, escolha 1 ou 2.")

if __name__ == "__main__":
    main()