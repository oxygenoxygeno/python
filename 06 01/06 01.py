a = set()
b = set()
c = input()
while c != '':
    a.add(c)
    c = input()
a.add(c)
c1 = input()
while c1 != '':
    b.add(c1)
    c1 = input()
intersection = a & b
if not intersection:
    print('EMPTY')
else:
    for i in intersection:
        print(i)