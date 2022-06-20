import random


def avg(n):
    mlist = [random.randint(-10, 10) for i in range(n)]
    print(*mlist)
    if n == 0:  # тогда - по факту, список пустой
        print(0)
        return 0
    else:
        print(sum(mlist) / len(mlist))
        return (sum(mlist) / len(mlist))


if __name__ == '__main__':
    n = int(input())
    avg(n)