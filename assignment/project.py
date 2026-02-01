# Mini Project: CLI E-Commerce Helper
# Scenario: Build a command-line interface (CLI) shopping program that:
# Displays a list of available products (stored in a Dictionary or List).
# Asks the user to input the name of a product to "add to cart".
# Stores selected items in a "cart" list.
# Calculates the total price of items in the cart.
# Applies a discount (e.g., 10%) if the total is over $100.
# Prints the final receipt.

print("CLI E-Commerce Helper")
available_products = {
    "mango": 30,
    "rice": 20,
    "tomatoe paste": 10,
    "beans": 15,
}

cart = []
user = input("Product to add to cart:")

if user not in available_products:
    print("Out of stock")
else:
    cart.append(user)

total_price = 0
for items in cart:
    total_price += available_products[items]
    if total_price > 100:
        discount = total_price * (10/100)

        final_price = total_price - discount
    else:
        final_price = total_price

receipt = (
    f"Items in cart: {cart}\n"
    f"Total price: Ghc{total_price}\n"
    f"Final price after discount:Ghc{final_price}"
)

print(receipt)
