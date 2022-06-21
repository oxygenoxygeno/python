p='''name = input()
print('Привет,', name) # здороваемся'''.split('\n')
print(*[i.rstrip() if not '#' in i else i[:i.index('#')].rstrip() for i in p],sep='\n')