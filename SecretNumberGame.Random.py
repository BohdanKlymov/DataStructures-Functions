from random import randint


num = randint(1,100)
numFromUser = 0

while numFromUser != num:
        print("Guess the number between 1 and 100.")
        numFromUser = int(input())
                
        if numFromUser > num:
                print("Not bad, but the number is less")
        elif numFromUser < num:
                print("Not bad, but the number is bigger")

print("You did it, nice work!")