n = int(input('n = '))
names = []
for i in range(n):
    names.append(input('-> '))
period = int(input('periond = '))
count = int(input('count = '))

for c in range(count):
    i = 0
    while i < len(names):
        names.pop(i)
        i += period - 1
print(names)