x = int(input())
y = int(input())
z = int(input())
n = int(input())
co = [1, 2, 3]
a = []
list1 = []

for i in range(0, x+1):
    for j in range(0, y+1):
        for k in range(0, z+1):
            co[0] = i
            co[1] = j
            co[2] = k
            a = co.copy()
            if((i+j+k) == n):
                continue
            else:

                list1.append(a)
print(list1)

# Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer .
#  Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to n. Here,
# Please use list comprehensions rather than multiple loops, as a learning exercise.
