# C. Problem 3: Creating a Shopping Cart
# Create a program that simulates a simple shopping cart. Use a dictionary cart to store items and their quantities. 
# The keys of the dictionary should be the item names (strings), 
# and the values should be the quantities (integers).

def show(cart: dict) -> str:
    Z = ""
    for x in cart:
        Z += x + ": " + str(cart[x]) + ", "
        
    Z = Z[:-2]
    return Z

def resolve(line, cart: dict):
    global return_s
    # add [item_name] [quantity]: Adds the specified item and quantity to the cart.
    # remove [item_name]: Removes the specified item from the cart.
    # show: Prints the current contents of the shopping cart.
    # The input ends when the user enters a "quit" command.
    command = line.split(" ")
    if len(command) == 3:
        if command[0] == "add":
            argument1 = command[1]
            argument2 = command[2]
            if argument1 in list(cart):
                cart[argument1] += int(argument2)
            else:
                cart[argument1] = int(argument2)
                
            print(f"{argument1}: {cart[argument1]}")
        else:
            print(0 / 0)
    elif len(command) == 2:
        
        if command[0] == "remove":
            argument1 = command[1]
            try:
                print(cart[argument1])
                del cart[argument1]
            except KeyError:
                print("Item not found")
        else:
            print(0 / 0)
            
            

# Input
# The input consists of multiple lines. Each line represents a customer interaction:
i = []
s = input()
while s != "quit":
    i.append(s)
    s = input()
# i = '''remove apple
# add apple 2
# add banana 1
# show
# add banana 10
# show
# remove banana
# show
# quit'''.split("\n")
cart = {}
while len(i) >= 1:
    line = i[0]
    i = i[1:]
    if line == "quit":
        break
    elif line == "show":
        # Output
        # For show, print the shopping cart as [item_name]: [quantity], with each item-quantity pair separated by a comma and space in ascending order of item names. If the cart is empty, print "Cart is empty."
        # For add, add or update the item in the cart, then print its name and quantity.
        # For remove, remove the item if it exists, then print its name and quantity. If it does not exist, print Item not found.
        # For quit, end the program and do not print anything.
        print(show(cart))
    else:
        resolve(line, cart)
