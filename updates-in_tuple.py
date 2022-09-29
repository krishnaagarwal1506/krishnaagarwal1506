tp = (1, 5, 10, 12, 17, 20)
list1 = list(tp)
for i in range(len(list1)):
    if list1[i] % 5 == 0:
        list1[i] += 5
tp1 = tuple(list1)
print(tp1)
# we have to convert in list and then make changes needed to be done in the list
# and then convert it to tuple again
