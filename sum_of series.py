# SERIES = [(1/1!)+(1/2!)+(1/3!)+(1/4!).......] =
a = int(input("enter the value of a:"))
sum = 0
n = 1
for i in range(1, (a+1)):
    for y in range(1, (i+1)):
        n = n*y
    sum += (1/n)

print(sum)
