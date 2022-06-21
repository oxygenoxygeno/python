s = 'Мир будет наш'
print(*['-'.join(map(str.upper,i)) for i in s.split()])