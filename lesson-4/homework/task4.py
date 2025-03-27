import random

x=random.randrange(0,100)
print
guess=False
while not guess:
    y=int(input("Guess: "))
    if y>x:
        print("too high")
    elif y<x:
        print("Too low")
    else:
        guess=True
        print("Correct")