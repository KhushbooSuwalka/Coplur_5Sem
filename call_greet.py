# ----------Importing a user made module----------------------
import greet
import Pydict
# greet.greeting("Alice")
greet.greeting(Pydict.dictionary["name"])

a=greet.sum(10,20)
print("Sum=",a)

b=greet.multiply(10,20)
print("Multiply=",b)

# ------------Importing in built math module--------------------
import math
n=16
k=5
# Combination formula: C(n, k) = n! / (k! * (n - k)!)
print("Combination C(", n, ",", k, ") =", math.comb(n, k))
print("Permutation P(", n, ",", k, ") =", math.perm(n, k))

print("Factorial of", n, "is", math.factorial(n))
print("Power of 2 raised to", k, "is", math.pow(2, k))
print("Truncated value of 3.14 is", math.trunc(3.14))

# ------------Importing in built datetime module--------------------
import datetime
x=datetime.datetime.now()
print("Current date and time:", x)
print("Current year:", x.year)
print(x.strftime("%B")) #Name of month
print(x.strftime("%A")) #Name of day

y=datetime.datetime(2020, 5, 17)
print("Specific date and time:", y)
print("Year of specific date:", y.year)