s = input()
a = ""
x = 0
for i in range(len(s)-1, -1, -1):
    a = a + s[i]
for i in range(0, len(a)):
    if(a[i] == s[i]):
        x = 1
        continue
    else:
        x = 0
        break
if(x == 0):
    print("not palindrom")
else:
    print("palindrom")
