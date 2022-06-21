from itertools import islice
import sys

n = int(input())
for line in islice(sys.stdin, n):
    if line.startswith("%%"):
        print(line[2:])
    elif not line.startswith('#' * 4):
        print(line)