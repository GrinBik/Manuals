def how_even(arr):
    res = 0
    for num in arr:
        if num % 2 == 0:
            res += 1
    return res


def unic(arr):
    res = []
    for i in arr:
        if res.count(i) == 0:
            res.append(i)
    return res


def letter(line):
    ans = {}
    for l in line:
        if l not in tuple(ans.keys()):
            ans[l] = 1
        else:
            ans[l] += 1
    return ans


test = [12, 54, 765, 354, 22, 433, 678, 854, 56, 211, 11, 101, 69]
print(how_even(test))

temp = [1, 1, 1, 1, 1, 3, 43, 43, 4, 3, 4, 9, 6, 7, 9, 7, 9, 5, 5, 5, 78, 9, 9, 9, 78, 6, 66, 6]
print(unic(temp))
print(set(temp))

poem = "Зайку бросила хозяйка -- Под дождем остался зайка. Со скамейки слезть не мог, Весь до ниточки промок."
rez = letter(poem)
print("В строке %s:" % poem)
for key in list(rez.keys()):
    print(f"{rez[key]} символов {key}")
