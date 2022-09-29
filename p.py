def lenOfConsecutiveSub(arr, n):
    ans = 0
    count = 0
    sett = set()

    for element in arr:
        sett.add(element)

    for element in arr:

        previousConsecutiveElement = element-1

        if(not previousConsecutiveElement in sett):
            j = element
            while j in sett:
                j += 1
            ans = max(ans, j-element)
    return ans


arr = input()
inrr = arr.split(',')
for i in range(len(inrr)):
    inrr[i] = int(inrr[i])
n = len(inrr)
if(lenOfConsecutiveSub(inrr, n) != 1):
    print(lenOfConsecutiveSub(inrr, n))
else:
    print(-1)
