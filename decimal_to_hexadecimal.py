n = int(input())
a = []
for i in range(1, n+1):
    a.append(i)
l = []

for i in range(1, n+1):
    l1 = []
    while (i != 0):
        m = (i % 16)
        if(m == 10):
            l1.append("A")
            i = i//16
        elif(m == 11):
            l1.append("B")
            i = i//16
        elif(m == 12):
            l1.append("C")
            i = i//16
        elif(m == 13):
            l1.append("D")
            i = i//16
        elif(m == 14):
            l1.append("E")
            i = i//16
        elif(m == 15):
            l1.append("F")
            i = i//16
        else:
            l1.append(m)
            i = i//16

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
    
