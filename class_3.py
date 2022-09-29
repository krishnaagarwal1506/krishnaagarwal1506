print("hello"+str(5))
# by default there is sep in print it create space between string
print("hello", "world")
# to change this sep keyword is used
print("hello", "world", sep='...')
# end keyword is for printing at the end of last string
print("hello", "world", sep='\n', end='...\n')
a = int(input("enter a no. a: "))
b = int(input("enter a no. b: "))
if(b > a):
    print("b is greater than a")

else:
    print("a is greater than b")
