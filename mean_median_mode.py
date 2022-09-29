n = int(input())
l = list(map(int, input().strip().split()))[:n]
s = 0
l.sort()
for i in l:
    s += i
mean = s/n
a = l[(n//2)-1]
if(n % 2 == 0):
    median = (l[(n//2)-1] + l[(n//2)])/2
else:
    median = (l[(n-1)//2])
print("{:.1f}".format(mean))
print("{:.1f}".format(median))
l1 = []
for i in l:
    l1.append(l.count(i))
l2 = []
for i in range(len(l1)):
    if(l1[i] == max(l1)):
        l2.append(l[i])
l2 = set(l2)
if(len(l2) == 1):
    l2 = list(l2)
    print(l2[0])
else:
    l2 = list(l2)
    print(min(l2))
