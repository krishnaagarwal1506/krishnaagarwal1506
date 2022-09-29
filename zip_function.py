rollno = (1, 2, 3)
name = ("kr", "ish", "na")
for i in zip(rollno, name):
    print(i)
rollno1 = (1, 2, 3, 4, 5)
for i in zip(rollno1, name):
    print(i)
# zip make pairs in both tuple
# it make pairs in refrence to the smaller tuple
l1 = [1, 2, 3]
l2 = [1, 2, 3, 4]
l3 = list(zip(l1, l2))
print(l3)
s1 = "krishna"
s2 = "agarwal"
s3 = list(zip(s1, s2))
s4 = tuple(zip(s1, s2))
print(s3)
print(s4)
zip()
# it return a zip object
a1 = [x for x in range(1, 11)]
a2 = [x*x for x in range(1, 11)]
a3 = [x*x*x for x in range(1, 11)]
result = list(zip(a1, a2, a3))
print(result)
# zip is a itrable data object
print(type(result[1]))
