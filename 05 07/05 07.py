n = int(input())
m = 'Остазия'
v = 'Евразия'
for i in range(n):
    s = input()
    if s == 'С кем война?':
        print(v)
    if s == 'С кем мир?':
        print(m)
    if s == 'Меняем':
        v1 = v
        v = m
        m = v1