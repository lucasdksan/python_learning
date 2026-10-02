def analyze_name():
    name = input('Digite seu nome: ')
    age = input('Digite sua idade: ')

    if not name or not age:
        print('Desculpe, você deixou campos vazios')
        return

    name_len = len(name)
    invert_name = name[::-1]
    space_in_name = ' ' in name
    first_letter = name[0]
    last_letter = name[name_len - 1]

    print(
        f'Seu nome {name}, seu nome invertido {invert_name}, '
        f'seu nome tem espaço {space_in_name}, seu nome tem {name_len} letras, '
        f'a primeira letra no seu nome {first_letter} e a última letra no seu nome {last_letter}'
    )


def format_examples():
    print('''
    s       - string
    d e i   - int
    f       - float
    x e X   - hexadecimal
    ''')


def assignment_operators():
    print('''
    Operadores de atribuição
    += -= *= /= //= **= %=
    ''')
