from itertools import permutations
s, n = input().split()
n = int(n)
a = list(permutations(s, n))
l1 = []
for i in a:
    l = list(i)
    l = "".join(l)
    l1.append(l)
l1.sort()
for i in l1:
    print(i)
# You are given a string(S) .
# Your task is to print all possible permutations of size(N)  of the string in lexicographic sorted order.
