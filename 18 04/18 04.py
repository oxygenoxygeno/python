def partialSums(*args):
    sums = [0]
    for i,x in enumerate(args):
            sums.append(x + sums[i])
    return sums

print(partialSums(1, 1/2, 1/4, 1/8, 1/16, 1/32))