N = int(input('Введите N: '))

strng = []
for i in range(N):
    strng.append(input(f'Введите {i + 1}-ю строку: '))

for i, strng in enumerate(strng):
    k = 0
    while True:
        k = strng.find('кот', k)
        if k == -1: break
        print(i + 1, k + 1)
        k += 1