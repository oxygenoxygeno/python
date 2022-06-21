s1 = 'питон'
s2 = 'пилот'
bulls = 0
cows = 0
for i in set(s1) & set(s2):
    if s1.index(i) == s2.index(i):
        bulls +=1
    else: cows += 1
print('bulls:',bulls,'cows:',cows)