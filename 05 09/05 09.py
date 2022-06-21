number = int(input())
number_1 = 0
for i in range(number):
    stroca = input()
    if 'кот' in stroca or 'Кот' in stroca:
        number_1 += 1
if number_1 > 0:
    print('МЯУ')
else:
    print('НЕТ')