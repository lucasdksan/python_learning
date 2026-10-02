a, b = 1, 3
b,a = a,b

print(a,b)

person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

address = {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA",
    "zip": "12345"
}

full_person_info = {**person, **address}

print(full_person_info)

def show_person_info(*args, **kwargs):
    print(args)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_person_info("John", 30, "New York", city="New York", state="CA", zip="12345")