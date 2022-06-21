x = int(input())
i = 1
while i <= x:
    i += 1
    y = input()
    if 'Кот' in y or 'кот' in y:
        t = True
        continue
if t == True:
    print('МЯУ')
else:
    print('НЕТ')