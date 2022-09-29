n = int(input().strip())
vals = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))
s = 0
for i in range(n):
    s += (vals[i]*weights[i])
w = 0
for i in weights:
    w += i
total = s/w
print("{:.1f}".format(total))
