a = 0
b = 1
next = 0
for i in range(1, 10):
    print(a)
    next = a+b
    a = b
    b = next
