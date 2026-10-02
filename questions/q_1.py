# Faça um programa que pede um número inteiro ao usuário

while True:
    value = input("Digite um número: ")

    if not value.isnumeric:
        print("Você não digitou um número")
        continue

    result = "Par" if int(value) % 2 == 0 else "Ímpar"

    print(f"Resultado {result}")

    continue_flow = input("Deseja continuar? [S]im ou [Não]")

    if not continue_flow.lower() == "s":
        print("Obrigado por executar aqui :D")
        break

    