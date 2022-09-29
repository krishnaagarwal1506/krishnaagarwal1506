from itertools import combinations
n = int(input())
l = []

for num in range(2, n + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            l.append(num)
l2 = []
print(l)
