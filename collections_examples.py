def list_names():
    names = ['Lucas', 'Aline', 'Alda', 'Leonardo']
    for index, name in enumerate(names):
        print(name, index)


def shopping_list_manager():
    shopping_list = []

    while True:
        input_option = input('Selecione uma opção \n [i]nserir [a]pagar [l]istar: \t').lower()

        if input_option.isnumeric() or input_option not in ('i', 'a', 'l'):
            print('Selecione apenas uma das opções!')
            continue

        if input_option == 'i':
            value = input('Digite o valor: ')
            shopping_list.append(value)
            continue

        if input_option == 'l':
            if len(shopping_list) == 0:
                print('Nada para listar')
                continue

            for index, value in enumerate(shopping_list):
                print(f'{index} {value}')
            continue

        if input_option == 'a':
            if len(shopping_list) == 0:
                print('Nada para apagar')
                continue

            index = input('Escolha o índice para apagar: ')

            if not index.isnumeric():
                print('Selecione apenas um dos índices')
                continue

            del shopping_list[int(index)]

            for item_index, value in enumerate(shopping_list):
                print(f'{item_index} {value}')
            continue
