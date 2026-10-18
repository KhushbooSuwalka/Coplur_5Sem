# A Number Guessing Game
import random

cnum=random.randrange(0,100)
count = 0

while True:
    unum = int(input("Enter your Number: "))
    count += 1

    if cnum > unum:
        print("Too Low! Try Again.")
    elif cnum < unum:
        print("Too High! Try Again.")
    else:
        print("Congratulations! You guessed the number correctly.")
        print("Total Attempts:", count)
        break