
a = []
n = int(input("enter thr no of elements of list:"))
for i in range(0, n):
    i = int(input("enter the {}th element of list:".format(i+1)))
    a.append(i)
print(a)
x = a[0]
for i in a[1:]:
    if(x > i):
        continue
    else:
        x = i
        ind = a.index(i)
print("largest element of list is {}".format(x))
# reason behind finding index of i is to assign a value to y so that we can compare it in loop and not to assign it the largest value
# it is more convinient than assigning is a very low no.(for eg. -999999999999999999999999999999999999999999)
if(ind == 0):
    y = a[1]
else:
    y = a[0]
for i in a:
    if(x == i):
        continue
    elif(y > i):
        continue
    else:
        y = i
print("Second largest element of list is {}".format(y))
