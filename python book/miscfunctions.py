#!python3

import math

rounding = 2.3
print("Ceiling of",rounding,": ",math.ceil(rounding))
print("Floor of",rounding,": ",math.floor(rounding))

base = 2
exponent = 5
print(base, "to the power of",exponent,": ",math.pow(base,exponent))

print("The square root of 64 is:  ", math.sqrt(64))


import random

print("Random number in the range 0 to 1:", random.random())
print("Random number in the range 0 to 100:", random.random() * 100)

print("Select lottery numbers:")
# Chooses 6 non-repeating numbers in the range 1 to 50
print("Your lucky numbers are: ", random.sample(range(1, 51),6))

value_one = 0.7
value_two = 1.05
first_result = value_one * value_two
second_result = value_one + first_result

print("Value one: ", "%.2f" % value_one)
print("Value two: ", "%.2f" % value_two)
print("First result: ", "%.2f" % first_result)
print("Second result: ", "%.2f" % second_result)


value_one = 0.7
value_two = 1.05
first_result = value_one * value_two
second_result = value_one + first_result

print("Value one: ", "%.20f" % value_one)
# Shows the number with 20 floating point digits
print("Value two: ", "%.20f" % value_two)
print("First result: ", "%.20f" % first_result)
print("Second result: ", "%.20f" % second_result)

import decimal

value_one = Decimal(0.7)
value_two = Decimal(1.05)
first_result = value_one * value_two
second_result = value_one + first_result

print("Value one: ", "%.2f" % value_one)
# Shows the number with 2 floating point digits
print("Value two: ", "%.2f" % value_two)
print("First result: ", "%.2f" % first_result)
print("Second result: ", "%.2f" % second_result)

from datetime import *

now = datetime.today()
print("Today: ",now)
print("Current time:  ", now.hour, ":", now.minute, sep="")
print("Today is a ", now.strftime("%A"),sep="")
print("The month is ", now.strftime("%B"),sep="")

from time import *

start = time()
start_time = localtime(start)
print("Started at: ", strftime("%X",start_time))

for i in range(0,10):
    print(i + 1)
    sleep(1) # Pauses for a second

end = time()
difference = end - start
print("The loop ran for", difference, "seconds.")






