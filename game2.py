# A Number Guessing Game
import random

cnum=random.randrange(0,100)
unum=int(input("Enter your Number:"))

if cnum>unum:
    print("Computer's Number is Greater than your Number")
elif cnum<unum:
    print("Computer's Number is Less than your Number")
else:
    print("Congratulations! You guessed the number correctly.")