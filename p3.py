def factorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return(f)


l = list(map(float, input().strip().split()))
n = l[0]
m = l[1]
a = n+m
p = n/a
q = m/a
s = 0
for i in range(3, 7):
    x = factorial(6)/(factorial(i)*factorial(6-i))
    y = p**i
    z = q**(6-i)
    s += (x*y*z)
print("{:.3f}".format(s))
