from sys import stdin
from re import search

n = 0
for line in stdin:
    if search('[Кк]апитан Ким', line):
        break
    n += 1

print(n)