from statistics import median
n = int(input().strip())
val = list(map(int, input().strip().split()))[:n]
freq = list(map(int, input().strip().split()))[:n]
l = []
for i in range(n):
    for j in range(freq[i]):
        l.append(val[i])

l.sort()
print(l)
if(len(l) % 2 == 0):
    l1 = l[:(len(l)//2)]
    print(l1)
    l2 = l[len(l)//2:]
    print(l2)
    m1 = median(l1)
    m2 = median(l2)
    print(m2-m1)
else:
    l1 = l[:(len(l)-1)//2]
    l2 = l[(len(l)+1)//2:]
    print(l1)
    print(l2)
    m1 = median(l1)
    m2 = median(l2)
    print(m2-m1)
