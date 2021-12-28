
Num1=float(input("Digite o primeiro número: "))
operação=input("digite a operação: ")
Num2=float(input("Digite o segundo número: "))

if operação == "+":
    resultado = (Num1 + Num2)
    print(f"o resultado é: {resultado}.")
elif operação == "-":
    resultado = (Num1 - Num2)
    print(f"o resultado é: {resultado}.")
elif operação == "/":
    resultado = (Num1 / Num2)
    print(f"o resultado é: {resultado}.")
elif operação == "*":
    resultado = (Num1 * Num2)
    print(f"o resultado é: {resultado}.")
elif operação == "%":
    resultado= (Num1/100) * Num2
    print(f"o resultado é: {resultado}.")
else:
    print("Operação invalida")

    