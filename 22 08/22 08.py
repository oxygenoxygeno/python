import random
import string


def passgen(n, nums):
    numeric = ([random.randint(-10, 10) for i in range(n)])
    numeric = str(numeric)
    numeric = numeric.replace('[', ' ')
    numeric = numeric.replace(']', ' ')
    numeric = numeric.replace(',', '')
    l = ''.join(random.choice(string.ascii_letters) for i in range(n))
    p = ''.join(random.choice(string.punctuation) for i in range(n))
    prom = numeric + l + p
    res = ''.join(random.sample(prom, len(prom)))
    # print(res)
    if nums == 1:
        res = numeric
        print(res)
        print('первая степень')
        return res

    elif nums == 2:
        prom = l + numeric
        res = ''.join(random.sample(prom, len(prom)))
        print(res)
        print('втораая степень')
        return res
    elif nums == 3:
        prom = numeric + l + p
        res = ''.join(random.sample(prom, len(prom)))
        print('третья  степень')
        print(res)

    else:
        print('wrong number')


if name == 'main':
    q = int(input("сколко паролей нужно?"))
    for i in range(q):
        n = 12
        nums = 3
        passgen(n, nums)