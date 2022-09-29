
n = int(input())
a = []
for i in range(1, n+1):
    a.append(i)
l = []

for i in range(1, n+1):
    l1 = []
    while (i != 0):

        m = (i % 2)

        l1.append(m)
        i = i//2
    l1.reverse()
    l.append(l1)
x = 0
for i in l:
    print(a[x], end=" ")
    print("->", end=" ")
    for j in i:
        print(j, end=" ")
    x += 1
    print()
