a = [1, 2, 3, 4, 5, 6, 7]


def num(a):
    total = 0
    for i in a:
        for j in a:
            print(j, i)  # o(n^2)
            total += 1   # o(n^2)
    return total


print(num(a))
# loop runs 49 times in this case
