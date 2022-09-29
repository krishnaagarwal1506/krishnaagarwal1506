n = int(input())
l = []
for i in range(n):
    a = int(input())
    l.append(a)
l1 = []
for i in l:
    j = i
    while (j < (i+5)):
        if(j % 5 == 0):
            if(j-i < 3):
                l1.append(j)
            else:
                l1.append(i)
        j += 1
for i in l1:
    print(i)
# ROUND OF TO MULTIPLE OF 5 IF REMAINDER IS GREATER THAN 3
