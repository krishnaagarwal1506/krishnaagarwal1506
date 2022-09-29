a = int(input("enter no a: "))
b = int(input("enter no b: "))
c = int(input("enter no c: "))
if(a > b and a > c):
    print("a is largest")
    if(b > c):
        print("c is smallest")
    else:
        print("b is smallest")
elif (b > c and b > a):
    print("b is largest")
    if(a > c):
        print("c is smallest")
    else:
        print("a is smallest")
else:
    print("c is largest")
    if(a > b):
        print("b is smallest")
    else:
        print("a is smallest")
