questions = [
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "response": "Brasília"
    },
    {
        "question": "Qual é o maior planeta do sistema solar?",
        "options": ["Marte", "Júpiter", "Terra", "Saturno"],
        "response": "Júpiter"
    },
    {
        "question": "Qual é o resultado de 7 x 8?",
        "options": ["54", "56", "58", "60"],
        "response": "56"
    },
    {
        "question": "Qual linguagem é conhecida por desenvolver páginas web?",
        "options": ["Python", "JavaScript", "C++", "SQL"],
        "response": "JavaScript"
    },
    {
        "question": "Qual é o animal que é o símbolo do Brasil?",
        "options": ["Tigre", "Papagaio", "Arara-azul", "Onça"],
        "response": "Arara-azul"
    }
]

count = 0
errors = 0
rights = 0

print("Vamos inciar")

while True:
    if count == len(questions):
        break

    print(f"Responda: {questions[count].get("question")}\nOpções: {questions[count].get("options")}")

    response = input()

    if response != questions[count].get("response"):
        print(f"Resposta Errada\n Resposta correta: {questions[count].get("response")}")

        count+=1
        errors+=1
        continue

    count+=1
    rights+=1
    print("Resposta Correta")

print(f"Resumo: \n Acertos: {rights} Erros: {errors}")

    