# EVERYTHING RELATED TO string
# IN PYTHON THERE IS NO SUCH THING AS CHARACTER ONLY STRING EXISTS (STR)
print("HELLO")
print('world')
a = "My name is:"
b = ' \"Krishna agarwal\"'
# to print double colons comsole we use escape meathod \"text\"
age = 18
# adding of 2 strings
print(a+b)
# for gap between string and string add (a+" "+b)
# three colons for multiline text(""")
c = """ Age = 18,
class= 1st year'
city = Anadra"""
print(c)
print(a+" "+b)
# slicing
print(b[1:8])
# if we leave last no. empty while declaring slice of string like (b[1:]) it will print string from a[1] to end of string
print(b[-15:-8])
# we can use negitive no. for counting from right side of the string for slicing
print(b.upper())
# to print any string into capital letters
print(b.lower())
# to print any string into small letters or we can use casefold function
print(b.strip())
# to remove any spaces from the front or the end of the string
print(b.split('a'))
# to split the string into 2 parts but the letter from which it is seperated will not be printed
print("my age is {}".format(age))
# FORMAT will print the string in the placeholders occured in the other  string
name = "ktishna agarwal"
print(name)
# in string we can change it whole but not letters
name = "krishna"
print(name)
# code written down will give error as string is inmutable as turpple
#name[1] = "r"
# print(name)
# capatalize is to make first letter capital
print(b.capitalize())
print(b.center(15))
# in center the no. represent the spaces both sides of the string
print(b.count(a))
# it count the no. of time the string written in the count comes in b
print(b.find("i"))
# it will tell index or position of letter i in the string b from left to right of all i
