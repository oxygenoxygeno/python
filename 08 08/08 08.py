s = 'pooppooop'
maxx = 0
temp = 0
for i in s:
    if i == 'o':
        temp += 1
        if temp > maxx:
            maxx = temp
    else:
        temp = 0
print(maxx)