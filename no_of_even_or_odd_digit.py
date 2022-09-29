a = int(input("enter the value of a:"))
even = 0
odd = 0
Esum = 0
Osum = 0
while(a != 0):
    n = (a % 10)
    a = (a//10)
    if(n % 2 == 0):
        even = even+1
        Esum = Esum+n
    else:
        odd = odd+1
        Osum = Osum+n
print("no. of even digits ", even)
print("sum of even digits ", Esum)
print("no. of odd digits ", odd)
print("sum of odd digits ", Osum)
