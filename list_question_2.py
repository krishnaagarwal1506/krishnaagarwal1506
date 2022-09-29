# Enter your code here. Read input from STDIN. Print output to STDOUT
# code to print which type od error whill (i/0),(i/variables)
t = int(input())
for i in range(0, t):
    a, b = input().split()
    if(a.isdigit()):
        if(b.isdigit()):
            a = int(a)
            b = int(b)
            if(b == 0):
                print("Error Code: integer division or modulo by zero")
            else:
                print((a//b))

        else:
            print("Error Code: invalid literal for int() with base 10: '{}'".format(b))
    else:
        print("Error Code: invalid literal for int() with base 10: '{}'".format(a))
