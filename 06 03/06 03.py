a = int(input())
b = int(input())
z = set()
x = set()
q = 0
for v in range(a):
    c = input()
    z.add(c)
for n in range(b):
    s = input()
    x.add(s)
count = len(z ^ x)
print(count if count > 0 else 'NO')