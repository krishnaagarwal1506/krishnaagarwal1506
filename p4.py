from itertools import combinations
n = int(input())
l = list(input().strip().split())[:n]
m = int(input())
ind = []
l2 = []
for i in range(n):
    l2.append(i)
print(l2)
for i in range(0, len(l)):
    if(l[i] == "a"):
        ind.append(i)
        l2.remove(i)
print(l2)


print(ind)
l1 = []
for i in range(n+1):
    l1.append(i)

y = combinations(l2, m)

x = combinations(l1, m)
for i in x:
    print(i)
