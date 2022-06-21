def count_down(n):
    if n == 0:
        print("Пуск!")
    else:
        print("Осталось", n)
        count_down(n - 1)


count_down(20)