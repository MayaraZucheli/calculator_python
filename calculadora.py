def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por 0 não é permitida."
    return x / y

def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        choice = input("Digite a escolha (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Primeiro número: "))
                num2 = float(input("Segundo número: "))
            except ValueError:
                print("Entrada inválida! Insira números válidos.")
                continue

            if choice == '1':
                print(f'{num1} + {num2} = {add(num1, num2)}')
            elif choice == '2':
                print(f'{num1} - {num2} = {subtract(num1, num2)}')
            elif choice == '3':
                print(f'{num1} * {num2} = {multiply(num1, num2)}')
            elif choice == '4':
                result = divide(num1, num2)
                if result == "Erro! Divisão por 0 não é permitida.":
                    print(result)
                else:
                    print(f'{num1} / {num2} = {result}')
        else:
            print("Escolha inválida! Selecione uma opção válida.")

        next_calculation = input("Deseja fazer outra operação? (s/n): ")
        if next_calculation.lower() != 's':
            print("Finalizando a calculadora. Obrigado!")
            break

calculator()
