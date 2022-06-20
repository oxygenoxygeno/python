def sumDig(n):
    if (n<10):
        return n
    else:
        return n%10+sumDig(n//10)