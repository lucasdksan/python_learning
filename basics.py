def greet_user():
    name = input('Digite seu nome: ')
    print(f'Olá, {name}. Estou aqui para te dar boas vindas')


def birth_date():
    day = input('Digite o dia do seu nascimento: ')
    month = input('Digite o mês do seu nascimento: ')
    year = input('Digite o ano do seu nascimento: ')

    print(f'Você nasceu no dia {day} no mês {month} de {year}. Correto?')


def sum_two_numbers():
    number_1 = input('Número 1: ')
    number_2 = input('Número 2: ')
    print(int(number_1) + int(number_2))


def operator_priority_examples():
    print('1 -> ()')
    print('2 -> **')
    print('3 -> * / // %')
    print('4 -> + -')


def check_input_types():
    user_input = input('Digite algo: ')

    print(
        f"Informações sobre o que você digitou: \n"
        f"É alfabético: {user_input.isalpha()}\n"
        f"É numérico: {user_input.isnumeric()}\n"
        f"É alfanumérico: {user_input.isalnum()}\n"
        f"É espaço: {user_input.isspace()}\n"
        f"Está em caixa alta: {user_input.isupper()}\n"
        f"Está em caixa baixa: {user_input.islower()}\n"
        f"Está em título: {user_input.istitle()}\n"
        f"É imprimível: {user_input.isprintable()}\n"
        f"É identificador: {user_input.isidentifier()}\n"
        f"É decimal: {user_input.isdecimal()}\n"
        f"É dígito: {user_input.isdigit()}"
    )


def bmi_calculator():
    name = input('Digite seu nome: ')
    age = input('Digite sua idade: ')
    weight = float(input('Digite seu peso: '))
    height = float(input('Digite sua altura: '))

    if height <= 0:
        print('Altura inválida. Digite um valor maior que zero.')
        return

    imc = weight / (height ** 2)
    print(f'O {name}, de {age} anos, possui um IMC de {imc:.2f}')


def compare_numbers():
    input_1 = input('Digite um valor: ')
    input_2 = input('Digite outro valor: ')

    if not input_1.isnumeric() or not input_2.isnumeric():
        print('Os valores não são números')
        return

    value_1 = int(input_1)
    value_2 = int(input_2)

    if value_1 > value_2:
        print(f'Primeiro valor {value_1} é maior que o segundo {value_2}')
    else:
        print(f'Segundo valor {value_2} é maior que o primeiro número {value_1}')
