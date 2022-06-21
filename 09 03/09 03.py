data = [input() for _ in range(int(input()))]

pos = int(input())

for text in data:
  if pos <= len(text):
    print(text[pos - 1], end='')