a = int(input("enter the no.:"))
if(a > 0):
    n = 0
    if(a == 2):
        print("2 is a prime no.")
    elif(a == 1):
        print("1 is not  prime no.")
    elif(a == 3):
        print("3 is a prime no.")
    else:
        for x in range(2, (a//2+1)):
            if((a % x) == 0):
                n = 0
                break
            else:
                n = 1
    if(n == 0):
        print("it is not a prime no")
    else:
        print("it is a prime no")
else:
    print("enter correct positive no.")
