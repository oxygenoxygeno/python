a = int(input())
b = input()
c = ' abcdefghijklmnopqrstuvwxyz'
res = []
len_c=len(c)
for i in b:
    res.append(c[(c.find(i)+a)%len_c])
print('Result: ', '"',''.join(res),'"', sep = '')