def main_print(data):
    print(*data, sep='\n')


data = [input() for i in range(int(input()))]
main_print(data)
print()
main_print(list(filter(lambda x: x.split()[1] in ('4', '5'), data)))