from basics import (
    birth_date,
    bmi_calculator,
    check_input_types,
    compare_numbers,
    greet_user,
    operator_priority_examples,
    sum_two_numbers,
)
from collections_examples import list_names, shopping_list_manager
from functions_examples import check_even_odd, closure_example, multiply_all, sum_values
from loops import hangman_game, matrix_loop, nested_loop_print, range_example
from strings_examples import analyze_name, assignment_operators, format_examples

EXAMPLES = {
    '1': ('Saudação', greet_user),
    '2': ('Data de nascimento', birth_date),
    '3': ('Soma de dois números', sum_two_numbers),
    '4': ('Prioridade de operadores', operator_priority_examples),
    '5': ('Tipos de entrada', check_input_types),
    '6': ('IMC', bmi_calculator),
    '7': ('Comparação de números', compare_numbers),
    '8': ('Análise de nome', analyze_name),
    '9': ('Formatos de strings', format_examples),
    '10': ('Operadores de atribuição', assignment_operators),
    '11': ('Matriz com while', matrix_loop),
    '12': ('Loop aninhado', nested_loop_print),
    '13': ('Range', range_example),
    '14': ('Jogo da forca', hangman_game),
    '15': ('Listagem de nomes', list_names),
    '16': ('Lista de compras', shopping_list_manager),
    '17': ('Soma de valores', sum_values),
    '18': ('Multiplicação com *args', multiply_all),
    '19': ('Par ou ímpar', check_even_odd),
    '20': ('Closure', closure_example),
}


def show_menu():
    print('Escolha um exemplo para executar:')
    for key, (label, _) in EXAMPLES.items():
        print(f'  {key} - {label}')
    print('  0 - Sair')


def main():
    while True:
        show_menu()
        choice = input('\nOpção: ').strip()

        if choice == '0':
            print('Até a próxima!')
            break

        item = EXAMPLES.get(choice)
        if item is None:
            print('Opção inválida. Tente novamente.')
            continue

        label, func = item
        print(f'\nExecutando: {label}\n')
        func()
        print()


if __name__ == '__main__':
    main()
