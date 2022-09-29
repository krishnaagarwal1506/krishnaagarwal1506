a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = []
for i in a:
    for j in b:
        l1 = (i, j)
        l.append(l1)
l = tuple(l)
for i in l:
    print(i, end=" ")
# cartesian product
# iT also have a inbuilt function (ITERTOOLS.PRODUCT)
