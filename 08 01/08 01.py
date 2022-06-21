slova = input()
minx = slova
maxx = slova
y = 'ДА'
n = 'НЕТ'
while True:
    slova = input()
    if slova == 'стоп':
        if len(set(minx) - set(maxx)) == 0:
            print(y)
            break
        else :
            print(n)
            break

    if len(slova) > len(maxx):
        maxx = slova
    if len(slova) < len(minx):
        minx = slova