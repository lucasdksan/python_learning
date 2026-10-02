s1 = set()

s1.add("Lucas")

print(s1)

s2 = { 1, 2, 3 }
s3 = { 3, 4, 5 }
s4 = { 2, 4, 6 }

s5 = s4 | s3
s6 = s4 & s2
s7 = s2 - s4
s8 = s5 ^ s4

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

list_save = list()

for i, line in enumerate(lista_de_listas_de_inteiros):
    for col in line:
        if not list_save.__contains__(col):
            list_save.append(col)

            if len(list_save) == len(line):
                print(f"Na linha {i} não foi encontrado valores repetidos")
                list_save.clear()

            continue

        print(f"A primeira repetição foi {col}")
        list_save.clear()
        break


