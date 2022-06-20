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