def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Não é possível dividir por zero")
    return a / b


if __name__ == "__main__":
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        operacao = input("Operação (+, -, *, /): ")

        if operacao == "+":
            print("Resultado:", somar(a, b))
        elif operacao == "-":
            print("Resultado:", subtrair(a, b))
        elif operacao == "*":
            print("Resultado:", multiplicar(a, b))
        elif operacao == "/":
            print("Resultado:", dividir(a, b))
        else:
            print("Operação inválida.")
    except ValueError as erro:
        print("Erro:", erro)
