import random

x=random.randrange(0,100)
print
guess=False
n=0
while not guess:
    y=int(input("Guess: "))
    if y>x:
        print("too high")
        n+=1
    elif y<x:
        print("Too low")
        n+=1
    elif n==10:
        print("you lost")
    else:
        guess=True
        print("Correct")