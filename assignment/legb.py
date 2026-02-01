# Fix the broken script where a local variable is accessed globally or modified incorrectly.
# Python
#total = 0

#def calculate_total():
#     discount = 10
#    total = total + discount 
#    print(f"Total inside: {total}")

#calculate_total()

#fixed
total = 0


def calculate_total():
    global total
    discount = 10
    total = total + discount
    print(f"Total inside: {total}")


calculate_total()
