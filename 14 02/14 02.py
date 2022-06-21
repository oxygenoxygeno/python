def space_game(text):
    a = []
    for i in range(len(text)):
        a.append(text[i])
    b = a.count(' ')
    if b % 2 == 0:
        print("Вы выиграли")
    else:
        print("Вы проиграли")