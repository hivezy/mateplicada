print("=" * 90)
print("MATEPLICADA")
print("Uma calculadora desenvolvida por Hivezy.")
print("Com a finalidade de auxiliar estudantes e profissionais em cálculos matemáticos, ")
print("esta ferramenta oferece uma interface simples e intuitiva para realizar operações básicas e avançadas.")
print("=" * 90)

print("\nCalculadora iniciada com sucesso!")

while True:
    try:
        num1 = float(input("Digite o primeiro número: ").strip().replace(",", "."))
        break

    except ValueError:
        print("\nErro: Por favor, digite um número válido.")

while True:

    print("\nEscolha a operação desejada:")
    print("+")
    print("-")
    print("*")
    print("/")

    opcao = input("\nDigite uma opção: ").strip().lower()

    if opcao == "+":
        print("\nVocê escolheu Adição.")
        break

    elif opcao == "-":
        print("\nVocê escolheu Subtração.")
        break

    elif opcao == "*":
        print("\nVocê escolheu Multiplicação.")
        break

    elif opcao == "/":
        print("\nVocê escolheu Divisão.")
        break

    else:
        print("\nIsso não é uma operação matemática. Revise")

while True:
    try:
        num2 = float(input("Digite o segundo número: ").strip().replace(",", "."))

        if opcao == "/" and num2 == 0:
            print(
                "\nErro: Divisão por zero não é operável."
                " Por favor, digite um número diferente de zero."
            )
            continue

        break
    except ValueError:
        print("\nErro: Por favor, digite um número válido.")

if opcao == "+":
    resultado = num1 + num2
    print(f"\nO resultado da adição é: {resultado}")

elif opcao == "-":
    resultado = num1 - num2
    print(f"\nO resultado da subtração é: {resultado}")

elif opcao == "*":
    resultado = num1 * num2
    print(f"\nO resultado da multiplicação é: {resultado}")

elif opcao == "/":
    resultado = num1 / num2
    print(f"\nO resultado da divisão é: {resultado}")