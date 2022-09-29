s = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]  # O(1)


def students(stu):
    print(stu[0])  # O(1)
    total = 0  # O(1)
    l = []  # O(1)
    for i in stu:
        total += 1  # O(n)
        l.append(i)  # O(n)
    print(l)  # O(1)
    return(total)  # O(1)


print(students(s))  # O(1)
# total = #O(7+2n)->O(n)
# as n is no. of inputs and generally  no. of inputs is very large (for eg. 7 + 2*2million),here 7 is insignificant
# efff
