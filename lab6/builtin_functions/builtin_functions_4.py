import time
def square_root(num, time1):
    time.sleep(time1/1000)
    return ("Square root of " + str(num) + " after " + str(time1) + " miliseconds is " + str(round(num**(1/2), 14)))

num = float(input("Write number: "))
time1 = int(input("Write time in miliseconds: "))
print(square_root(num, time1))
