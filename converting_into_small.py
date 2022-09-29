a = "KRISHNA AGARWAL"
for i in a:

    if ord(i) >= 65 and ord(i) <= 90:
        asci = ord(i)
        asci += 32
        # space ascci value also get minused so we have to exclude it
        print(chr(asci), end="")
    else:
        print(i, end="")
