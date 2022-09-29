n = int(input())
l = []
for i in range(1, n+1):
    l.append(i)
l1 = []
for i in range(1, n+1):
    l2 = []

    while (i != 0):
        m = (i % 2)

        l2.append(m)
        i = i//2
    l2.reverse()
    l1.append(l2)
l3 = []
for i in range(1, n+1):
    l4 = []

    while (i != 0):
        m = (i % 8)

        l4.append(m)
        i = i//8
    l4.reverse()
    l3.append(l4)
l5 = []

for i in range(1, n+1):
    l6 = []
    while (i != 0):
        m = (i % 16)
        if(m == 10):
            l6.append("A")
            i = i//16
        elif(m == 11):
            l6.append("B")
            i = i//16
        elif(m == 12):
            l6.append("C")
            i = i//16
        elif(m == 13):
            l6.append("D")
            i = i//16
        elif(m == 14):
            l6.append("E")
            i = i//16
        elif(m == 15):
            l6.append("F")
            i = i//16
        else:
            l6.append(m)
            i = i//16

    l6.reverse()
    l5.append(l6)
for i in range(0, len(l)):
    print(l[i], end=" ")
    for j in l3[i]:
        print(j, end="")
    print(" ", end=" ")
    for j in l5[i]:
        print(j, end="")
    print(" ", end=" ")
    for j in l1[i]:
        print(j, end="")
    print(" ", end=" ")
    print()
# converting without default function
