# class 1
import sys
a = 10
print(id(a))
b = 20
print(a+b)
print(type(a))
a = 10.5
print(type(a))
# only string no charecter even single letter is a string so class 'STR' only works
s = "hello"  # same as 'hello'
print(s)
# CLASS 2
print(id(a))
# it totally depends on system how much size is given to any variable or no.
print(sys.getsizeof(0))
print(sys.getsizeof(1))
print(sys.getsizeof(2000.566))
print(sys.getsizeof(a))
print(sys.getsizeof(s))
# by default input is string so we use typecasting
a = int(input("enter the value of a\n"))
b = int(input("enter the value of b\n"))
print(a+b)
print(a-b)
print(a % b)
print(a/b)
print(a//b)
print(a*b)
