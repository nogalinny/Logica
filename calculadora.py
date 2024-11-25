def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero não é permitida."

def calculadora():  
    print('Bem-vindo a calculadora Python!')

while True:
        # Menu de operações
        print("\nEscolha uma operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Sair")
        
  # Recebe a escolha do usuário
        operacao = input("Digite o número da operação desejada: ")

        if operacao == '5':
            print("Saindo da calculadora. Até mais!")
            break

        # Recebe os números de entrada do usuário e converte para float
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue

        # Verifica e executa a operação escolhida
        if operacao == '1':
            resultado = adicionar(num1, num2)
            print(f"\nResultado: {num1} + {num2} = {resultado}\n")
        elif operacao == '2':
            resultado = subtrair(num1, num2)
            print(f"\nResultado: {num1} - {num2} = {resultado}\n")
        elif operacao == '3':
            resultado = multiplicar(num1, num2)
            print(f"\nResultado: {num1} * {num2} = {resultado}\n")
        elif operacao == '4':
            resultado = dividir(num1, num2)
            print(f"\nResultado: {num1} / {num2} = {resultado}\n")
        else:
            print("Operação inválida! Tente novamente.\n")

# Executa a calculadora
calculadora()