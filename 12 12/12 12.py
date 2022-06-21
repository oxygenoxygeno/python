s = input().lower()
n = 0
for i in range(len(s)):
    if s.count(s[i]) > n:
        n = s.count(s[i])
print(n)