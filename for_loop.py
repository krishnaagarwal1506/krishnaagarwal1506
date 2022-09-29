a = int(input("enter the value of a:"))
print("------------------------------------------------------------------------")
# normal triangle
for x in range(0, (a+1)):
    print("*"*x)
print("------------------------------------------------------------------------")
# triangle of even *
for x in range(0, (a+1), 2):
    print("*"*x)
print("------------------------------------------------------------------------")
# triangle of odd *
for x in range(1, (a+1), 2):
    print("*"*x)
print("------------------------------------------------------------------------")
# downward triangle
for x in range((a+1), 0, -1):
    print("*"*x)
print("------------------------------------------------------------------------")
# triangle staring from right
for x in range((a+1), 0, -1):
    print(" "*x + "*"*((a+1)-x))
print("------------------------------------------------------------------------")
for x in range((a+1), 0, -1):
    print(" "*x + "*"*((a+1)-x) + "*")
print("------------------------------------------------------------------------")
for x in range(0, a):
    for y in range(0, x+1):
        print(x+1, end=" ")
    print()
print("------------------------------------------------------------------------")
for x in range(0, a):
    i = 1
    for y in range(0, x+1):
        print(i, end=" ")
        i = i + 1
    print()
print("------------------------------------------------------------------------")
s = 'A'
for x in range(a):
    for y in range(0, x+1):
        # print have default function of new line
        print(s, end=' ')
        # we have to convert the char to no. and then increment it and then covert it into char again
        s = chr(ord(s) + 1)
    print()
print("------------------------------------------------------------------------")
for x in range(0, a+1):
    n = (x+1)
    for i in range(0, (a+1)-x):
        print(" ", end=" ")

    for y in range(0, x+1):
        print(n, end=" ")
        n = n-1
    print()
for i in range(i, a+1):
    print("💩"*i)
