a = []
c = []
name = []
n = int(input())
for i in range(0, n):
    b = []
    for j in range(0, 2):
        x = input()
        b.append(x)

    a.append(b)
for i in range(0, n):
    a[i][1] = float(a[i][1])
    c.append(a[i][1])
y = c[0]
for i in c:
    if(y < i):
        continue
    else:
        y = i
for i in range(0, n):
    if(y == a[i][1]):
        c.pop(c.index(a[i][1]))
    else:
        continue
y = c[0]
for i in c:
    if(y < i):
        continue
    else:
        y = i
for i in range(0, n):
    if(y == a[i][1]):
        name.append(a[i][0])

    else:
        continue
name.sort()
for i in name:
    print(i)
# Given the names and grades for each student in a class of N students,
#  store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
