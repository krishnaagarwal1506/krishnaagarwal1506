from statistics import mean
import math
n = int(input().strip())
vals = list(map(int, input().strip().split()))[:n]
s = 0
vals.sort()
m = mean(vals)
for i in vals:
    a = (m-i)**2
    s += a
sd = s/len(vals)
sd = math.sqrt(sd)
print("{:.1f}".format(sd))
