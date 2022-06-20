import string
import random

group = []
for i in string.ascii_letters:
    if i != "l" and i != "I" and i != "o" and i != "O":
        group.append(i)
        random.shuffle(group)
for j in string.digits:
    if j != "1" and j != "0":
        group.append(j)
        random.shuffle(group)


def generate_password(m):
    a = []
    for _ in range(1, m + 1):
        a.append(str(random.choice(group)))
    a = "".join(a)
    return a


def main(n, m):
    group2 = []
    for q in range(1, n + 1):
        group2.append(generate_password(m))
    return group2