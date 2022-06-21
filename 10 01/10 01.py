from itertools import combinations
from operator import mul

n = int(input())
a = [int(input()) for _ in range(n)]
p = int(input())

flag = any(p == mul(*combination) for combination in combinations(a, 2))
print("ДА" if flag else "НЕТ")