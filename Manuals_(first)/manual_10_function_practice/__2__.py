def unic(arr):
    res = []
    for i in arr:
        if res.count(i) == 0:
            res.append(i)
    return res


temp = [1, 1, 1, 1, 1, 3, 43, 43, 4, 3, 4, 9, 6, 7, 9, 7, 9, 5, 5, 5, 78, 9, 9, 9, 78, 6, 66, 6]
print(unic(temp))

print(set(temp))
