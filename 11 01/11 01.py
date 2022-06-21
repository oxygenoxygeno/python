T = input()
T = T.split()
K = 0
for slovo in T:
    K += 1
    if K % 3 == 0:
        print(slovo, ' ', sep='', end='')