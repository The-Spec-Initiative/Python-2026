# Create a basic script hello.py that, when run,
# prints "Welcome to our Python program!" to the terminal.
import random
print("Welcome to our Python program!")

# Create variables for user_name, user_age, and is_logged_in,
# then print a formatted sentence using an f-string: "User [Name], age [Age], is logged in: [True/False]".
user_name = "Ella"
user_age = 19
is_logged_in = True
print(f"User {user_name}, age {user_age}, is logged in: {is_logged_in}")

# Build a simple discount checker script. Define a variable age and is_logged_in.
# Print True if the user is 18+ andlogged in.
age = 17
is_logged_in = True

if age >= 18 and is_logged_in:
    print(True)
else:
    print(False)

# Create a script that checks a variable role ("admin", "user", "guest")
# and prints a custom welcome message for each using if/elif/else.
role = input("What's your role? ")

if role == "admin":
    print("Welcome Admin!")
elif role in ("user", "guest"):
    print("Welcome!!")
else:
    print("Role not found!")

# Write a function calculate_total(price_a, price_b)
# that adds two prices and returns the total. Call it and print the result.


def calculate_total(a, b):
    return a + b


a = int(input("Type first price"))
b = int(input("Type second price"))

total = calculate_total(a, b)
print(f"The total price is {total}")

# Create a list of numbers. Use a method to add a new number to the end,
# then print only the first 3 numbers using slicing.

numbers = [1, 2, 3, 4]
(numbers.append(5))
print(numbers)
print(numbers[: 3])

# Create a product dictionary with keys: name, price, and in_stock.
# Print a string saying "The [name] costs $[price]".

product = {
    "name": "apple",
    "price": 40,
    "in_stock": True,
}

print(f"The {product['name']} cost ${product['price']}")

# Create a list of user names.
# Use a for loop to print "Hello, [Name]" for each user in the list.
names = ["Ama", "Kofi", "Kwaku", "Ana"]

for name in names:
    print(f"Hello, {name}")

# Build a script that asks the user for their name and favorite color,
# then prints a message in all uppercase letters.

name = (input("WHat's your name?"))
color = (input("What's your favorite color?"))

print(f"My name is {name} and my favorite color is {color}" .upper())

# Write a script that asks the user for a "note to self",
# saves it to a text file named notes.txt,
# and then reads the file back to the console.

note = input("Write a note to self: ")

with open("notes.txt", "w") as file:
    file.write(note)

with open("notes.txt", "r") as file:
    print("Your note:")
    print(file.read())

# Import the random module to create a simple "Guess the Number"
# game where the computer picks a number between 1-10.


number = random.randint(1, 10)
guess = int(input("Guess a number between 1 and 10:"))

if guess == number:
    print("Correcttt!!")
else:
    print(f"Wrong!! The number was {number}")


# Write a calculator that asks for two numbers and divides them.
# Use try...except to catch the error if the user tries to divide by zero.


try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1 / num2
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Enter valid numbers!")
else:
    print(f"Result: {result}")
finally:
    print("Calculation complete.")
