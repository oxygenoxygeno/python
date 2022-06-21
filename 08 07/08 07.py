a = int(input())
for n in range(a):
    b = input()
    if b.find('кот') != -1:
        print(n + 1, b.find('кот') + 1)