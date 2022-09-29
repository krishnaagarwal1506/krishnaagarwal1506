# LIST
# in list we can change its values to anythings
# list can store different types of datatype values
names = ["mishu", "mannu", "manthan", "sakshi",
         "ishu", "monty", "ayushi", "monu"]
print(names)
print(names[0:4])
print(names[:5])
# same as strings
print(names[1:])
if "ishu" in names:
    print("exist")
else:
    print("does not exist")
names[0] = "krishna"
print(names)
names[2:5] = ["ansh", "mnthan", "sandi", "mahi"]
print(names)
# Append functions
list = [1, 2, 3]
list.append(4)
print(list)
list2 = [5, 6, 7]
list.append(list2)
print(list)
# list2 is mnested list in list 1
# list[4] is a whole unit ae list2
print(list[4][1])
# how to get acess or print the value in nested list
list3 = [[[1, 2, 3]]]
print(list3)
print(list3[0])
print(list3[0][0])
print(list3[0][0][0])
# extend only work on iterable object
list.extend("89")
print(list)
# here list is a iterable object whhile "89" is a string
list.extend(list3)
print(list)
# nested list is counted as a whole single unit in the list
print(len(list))
a = list
print(a)
a.append(9)
print(list)
# list and a points towards same list and address so change in one will lead to change in another automatically
# so to perform changes to the list while leaving th orignal ths same we have to copy that list and perform changes in new copied list

# (remove) function is to remove any data from list with help of value and pop fuction is to delete the data through value of index
# in (pop) if index is not given or bigger than present in list then it will remove the last data from end
# in remove if value comes for more than 1 time it will only remove the value that come first
# (clear) function will remove all data from list
list4 = ["i","like","you"]
print(list4);
print(list4[1]);
print(list4[-1]);
print(list4[:2]);
print(list4[1:]);
print(list4[0:-1]);
