n = int(input("Enter number of elements : "))
# one meathod to take input in list
#l = list(((input()).strip().split()))[:n]
l = []
for i in range(0, n):
    ele = int(input())
    l.append(ele)

print(l)
l1 = l.copy()
print(l1)

a = l.index(3)
l1[0] = 25
print(l1)
print(l)
print(a)
