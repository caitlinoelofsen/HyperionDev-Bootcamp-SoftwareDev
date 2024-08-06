import math
# Request triangle measurements from user
a = int(input("Input length A of triangle: "))
b = int(input("Input length B of triangle: "))
c = int(input("Input length C of triangle: "))
# Calculate area of triangle
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print(area)
# I used the following article to help me understand the formula above to solve the area: https://unstop.com/blog/area-of-triangle-in-python