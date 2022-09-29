# TURPLES
# turple can store different datatypes values
# turple values cannot be changed,they are unmuteble
# we can change turple by whole, not any of its parts as mentioned above
turple = ('a', 'b', 'c', 'd', 'e', 'f')
print("a = ", turple)
# error
#turple[2] = 1
# print(turple)
tur = ('a', 'b', 'c', '1+2j', '1.5', '1')
print("b = ", tur)
turple = ('a', 'b', 'c', 'd', 'e')
print("c = ", turple)
print(tur.__sizeof__())
tp = (x for x in range(100) if(x % 2 == 0))
for i in tp:
    print(i)
