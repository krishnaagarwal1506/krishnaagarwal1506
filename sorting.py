a = []
b = []
c = []
n = int(input("enter thr no of elements of list:"))
for i in range(0, n):
    i = int(input("enter the {} th element of list:".format(i+1)))
    a.append(i)
print(a)
while(a != c):
    x = a[0]
    for i in a[0:]:
        if(x > i):
            continue
        else:
            x = i
    b.append(x)
    a.pop(a.index(x))

for i in range(n-1, -1, -1):
    c.append(b[i])

print("list is sorted in decending order : {}".format(b))
print("list is sorted in accendind order : {}".format(c))
