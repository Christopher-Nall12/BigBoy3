# Approximations of Pi
# Math Module

print(22/7)
print(355/113)

import math

print(9801/(2206 * math.sqrt(2)))

def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    onehalfSides = math.sin(math.radians(halfAngleA))
    sides = onehalfSides * 2
    polygonCircumference = numSides * sides
    pi = polygonCircumference / 2
    return pi


print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(40, 400, 40):
    print(sides, archimedes(sides))


# See the loop above. In addition to the value of pi, print the difference
# between the values calculated by the archimedes function and by math.pi.
# How many sides does it take to make the 2 functions closer

# The difference is -3.98741751768128e-05

# The numbers you use are 40 million, 400 million, 40 million in the archimedes program.

for sides in range(40, 400, 40):
    print(sides, archimedes(sides))

print(3.1415527794146163-3.141592653589793)


for sides in range(40000000, 400000000, 40000000):
    print(sides, archimedes(sides))

print(math.pi)



# Accumulators

# accumulators hold the value that was added and keeps stacking and the value keeps going starting from the x value (x,y) and does not include
# the value.

acc = 0
for val in range(1, 6):
    acc = acc + val

print(acc)

acc = 0
for val in range(2, 20):
    acc = acc + val

print(acc)

# by adding a third number you are telling the computer to count by that certain number
# the second number is the number that is greater than the last number of your sequence but not equal

acc = 0
for val in range(0, 201, 2):
    acc = acc + val
#          start    Number greater than    what to count by
print(acc)

acc = 0
for val in range(1, 101, 2):
    acc = acc + val

print(acc)

acc = 0
for val in range(1, 201, 2):
    acc = acc + val / 100

# The computer does not care about putting parentheses it always does the equation from left to right
# making it say the accumulative added by the value and then being divided by 100

print(acc)



acc = 0
N = acc + 3

for val in range(N, 101, 2):
    acc = acc + val

print(acc)

factorial = N
for val in range(N, 101):
    factorial = val + factorial
print(factorial)

acc = 0
for val in range(1, 11):
    acc = val + acc
print(acc)



# Compute the sum of the first 100 even numbers     10100

# Compute the sum of the first 50 odd numbers       2500

# Compute the average of the first 100 odd numbers  100.0
# Write a function that returns the average to the first N numbers, where N is the parameter    I made N = to acc + 3. By doing that
# it is raising the value of N every time.

# Write a function called fractorial that computes the product of the first N numbers, where the N is a Parameter.
# factorial = N
# for val in range(N, 101):
#     factorial = val + factorial
# print(factorial)

# Each number in the Fibonacci sequence is the sum of the previous two numbers.
# acc = 0
# for val in range(1, 11):
#     acc = val + acc
# print(acc)
# The first two numbers in the sequence are 1 and 1.  Compute the 10th Fibonacci number.  55

# Write a function to compute the Nth Fibonacci number, where N is a parameter.
# You may assume that N will be greater than or equal to 3.    Depending on what value you give to the variable(N) it will vary your answer
# If you have a rule that the variable is greater than or equal to 3 then you can use and positive integer greater or equal to 3.

N = 3
acc = 0
for val in range(1, N):
    acc = val + acc
print(acc)



# Monte Carlo Simulation
# Random Numbers

import random

print(random.random())
