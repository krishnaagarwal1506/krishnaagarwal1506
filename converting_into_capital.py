a = "krishna agarwal"
for i in a:

    if ord(i) >= 97 and ord(i) <= 122:
        asci = ord(i)
        asci -= 32
        # space ascci value also get minused so we have to exclude it
        print(chr(asci), end="")
    else:
        print(i, end="")
