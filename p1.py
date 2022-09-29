a = int(input())
b = int(input())
while(a > 1 and a < b):
    x = 0
    if(a == 2):
        x = 1
    else:
        for i in range(2, a):
            if(a % i == 0):
                x = 0
                break
            else:
                x = 1

    if(x == 1):
        break
    a = a+1
while(b > 1 and b > a):
    x = 0
    if(b == 2):
        x = 1
    else:
        for i in range(2, a):
            if(b % i == 0):
                x = 0
                break
            else:
                x = 1
    if(x == 1):
        break

    b = b-1
if(a == b and x == 1):
    print(0)

else:
    print(b-a)
