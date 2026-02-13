# Gives 3 tries, 1 check if the number i input is greater or less than the random number number generated
#2  9
#rand number is greater than 2( 1)
####9 break out i won
#5
# rand number is greater than 5(2)
# 6 rand numner is greater than 6(3)
#game over(3)
import random

number = int(random.randint(1, 10))

for i in range(3):
    guess = int(input("Guess a number between 1 and 10:"))
    if guess < number:
        print(f"Enter a higher number")
        print("no of tries left: ")
    elif guess > number:
        print(f"Enter a Lesser Number")
    print("no of tries left: ")
    if guess == number:
        print("Correcttt!!")
        print(f"took: {} tries ")
        break
    print(f"Wrong!")
else:
    print(f"Game over {number}")

print(f"Random number is {number}")
