n, m = map(int, (input()).split())
arr = list(map(int, input().strip().split()))[:n]
a = list(map(int, input().strip().split()))[:m]
b = list(map(int, input().strip().split()))[:m]
a = set(a)
b = set(b)
h = 0
for i in a:
    for j in arr:
        if(i == j):
            h += 1
        else:
            continue
for i in b:
    for j in arr:
        if(i == j):
            h -= 1
        else:
            continue
print(h)
# it have long running tine so we can use
# print(sum[(i in a)-(i in b) for i in arr])
# as conditiob true means (true==1) & (false==0)
