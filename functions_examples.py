def sum_values(x, y):
    print(x + y)


def multiply_all(*args):
    total = 1
    for value in args:
        total *= value
    return total


def check_even_odd(*args):
    for value in args:
        print(f'{value} é par' if value % 2 == 0 else f'{value} é ímpar')


def multiply_by(value_1):
    def execute(value_2):
        return value_1 * value_2
    return execute


def closure_example():
    step_1 = multiply_by(5)
    result = step_1(5)
    print(result)
