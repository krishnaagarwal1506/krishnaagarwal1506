import math
ab = int(input())
bc = int(input())
hypo = math.hypot(ab, bc)
angle = round((math.degrees(math.acos((bc)/hypo))))
print(angle, chr(176), sep="")
# ABC is a right triangle,90 at B .
# Point M is the midpoint of hypotenuse .
# You are given the lengths AB and BC .
# Your task is to find ANGLE(MBC) in degrees.
