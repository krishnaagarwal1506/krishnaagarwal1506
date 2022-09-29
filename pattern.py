a = int(input("enter the value of a:"))

n = 1
m = 1
for i in range(0, a):
    for j in range(0, i+1):
        print(n, end=" ")
    n = n+1
    for x in range(((a-i)*2)-2, 0, -1):
        print(" ", end=" ")
    for j in range(0, i+1):
        print(m, end=" ")
    m = m+1

    print()
