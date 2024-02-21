import math
num = int(input("Input number of sides: "))
length = float(input("Input the length of a side: "))

area = (num * length ** 2) / (4 * math.tan(math.pi / num))


print("The area of the polygon is:", area)
