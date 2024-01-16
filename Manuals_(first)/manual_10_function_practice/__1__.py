def how_even(arr):
    res = 0
    for num in arr:
        if num % 2 == 0:
            res += 1
    return res


test = [12, 54, 765, 354, 22, 433, 678, 854, 56, 211, 11, 101, 69]
print(how_even(test))
