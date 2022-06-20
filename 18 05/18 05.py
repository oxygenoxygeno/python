scoring = {'Яблочко': 50, 'Зеленое_кольцо': 25,
'Внешнее_кольцо': {1: 8, 2: 6, 3: 42, 20: 50},
'Внутреннее_кольцо': {1: 2, 2: 16, 3: 56, 20: 3}}


def score(a, b=0):
    global scoring
    if not b:
        if a == 'Яблочко':
            return 50
    elif a == 'Зеленое_кольцо':
        return 25
    else:
        if a == 'Внешнее_кольцо':
            return scoring[a][int(b)]
        elif a == 'Внутреннее_кольцо':
            return scoring[a][int(b)]

print(score("Внешнее_кольцо", 1))