person_list = [
    { "name": "Lucas da Silva", "age": 18 },
    { "name": "Aline Adelaide Silva Lima", "age": 16 },
]

person_list.sort(key= lambda item: item["age"])

print(person_list)

def execute(fun, *args):
    return fun(*args)

print(execute(lambda x, y: x +y, 5, 6))