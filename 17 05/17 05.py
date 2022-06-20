def mirror(arr):
    arr[:] = arr + arr[::-1]
    return arr


arr = [1,2]
mirror(arr)
print(*arr)
