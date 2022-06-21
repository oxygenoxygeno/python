n = int(input())
a = list()
for i in range(n):
    s = int(input())
    a.append(s)
p = int(input())
q = int(input())
print(sum(a[p - 1:q]))