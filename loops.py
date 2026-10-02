def matrix_loop():
    cols = 10
    rows = 10

    count_col = 0
    count_row = 0

    while count_row < rows:
        while count_col < cols:
            print(f'matrix-> linha = {count_row} coluna = {count_col}')
            count_col += 1

        count_row += 1
        count_col = 0

    print('Fim do loop')


def nested_loop_print():
    linhas = 2
    colunas = 2

    linha = 1
    while linha <= linhas:
        coluna = 1
        while coluna <= colunas:
            print(linha, coluna)
            coluna += 1
        linha += 1


def range_example():
    numbers = range(10)
    for number in numbers:
        print(number)


def hangman_game():
    secret_word = 'marmota'
    show_word = '*' * len(secret_word)

    while True:
        if show_word == secret_word:
            break

        input_letter = input('Digite uma letra: ')

        if len(input_letter) > 1 or not input_letter.isalpha():
            print('Digite apenas uma letra')
            continue

        if secret_word.find(input_letter) < 0:
            print(f'A letra {input_letter} não está na palavra')
            print(show_word)
            continue

        temp_word = ''
        for letter in secret_word:
            if letter == input_letter:
                temp_word += letter
            else:
                temp_word += '*'

        aux_word = ''
        for i in range(len(secret_word)):
            if show_word[i] == temp_word[i]:
                aux_word += show_word[i]
            elif show_word[i] == '*' and temp_word[i] != '*':
                aux_word += temp_word[i]
            elif show_word[i] != '*' and temp_word[i] == '*':
                aux_word += show_word[i]

        show_word = aux_word
        print(show_word)

    print('Parabéns, você acertou: ', secret_word)
