# Gives 3 tries, 1 check if the number i input is greater or less than the random number number generated
# 2  9
# rand number is greater than 2( 1)
# 9 break out i won
# 5
# rand number is greater than 5(2)
# 6 rand numner is greater than 6(3)
# game over(3)
import random

player = input("What's your name?")
play_again = True

while play_again:
    number = random.randint(1, 10)
    tries = 3

print(f"Welcome {player} to the Guess the Number Game!"
      f"You have only {tries} tries to guess the number between 1 and 10."
      f"Use the hints wisely to help you win the game!!")

for attempt in range(1, tries + 1):
    guess = int(input(f"{player}, guess a number between 1 and 10:"))

    if guess == number:
        print(f"{player} you won!!")
        break
    elif guess < number:
        print(f"{player}, Enter a higher number")
    elif guess > number:
        print(f"{player}, Enter a lesser number")

else:
    print(f"Game over {player}! The number was {number}")

again = input("Do you want to play again? (yes/no): ").strip().lower()
if again != "yes":
    play_again = False
    print(f"Thanks for playing, {player}! byeee!")
