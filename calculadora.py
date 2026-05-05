def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b


def menu():
    print("=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")


def main():
    menu()
    
    opcao = input("Escolha uma operação: ")

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except:
        print("Erro: Digite apenas números!")
        return

    if opcao == "1":
        print("Resultado:", soma(num1, num2))
    elif opcao == "2":
        print("Resultado:", subtracao(num1, num2))
    elif opcao == "3":
        print("Resultado:", multiplicacao(num1, num2))
    elif opcao == "4":
        print("Resultado:", divisao(num1, num2))
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
