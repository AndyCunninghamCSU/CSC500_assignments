# Andrew Cunningham
# CSC 500 - Module 6 Porfolio Milestone

# Implements a terminal interface for the shopping cart class

from ShoppingCart import ShoppingCart
from ItemToPurchase import ItemToPurchase
import shlex

def print_menu():
    '''prints the menu -> nothing'''
    print("MENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Modify Item")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - Quit")
    print("t - test")

def handle_command(command, shopping_cart):
    ''' input the command straight off the terminal input and the shopping cart
        attempts to interpret the command and returns the needed function
        updates the shopping cart
    '''
    commands = {
        'a': shopping_cart.add_item,
        'r': shopping_cart.remove_item,
        'c': shopping_cart.modify_item,
        'i': shopping_cart.print_descriptions,
        'o': shopping_cart.print_total,
        't': shopping_cart.test_cart
    }

    if command:
        # split the input into a list of commands seperted by space, using shlex to account for quotes
        # around item name and description
        command_list = shlex.split(command)
        action = command_list[0]
        args = command_list[1:]

        if action == 'q':
            # simple implementation of quit
            return 'q'

        # look up the function that corresponds to the command
        func = commands.get(action, lambda *args, **kwargs: print("Invalid Command"))

        if action in ['a', 'r', 'c'] and not args:
            print("Error, see usage")
        else:
            # this implementation is simple, if it conmtains args then we have to make an item, otherwise there
            # are no args
            if args:
                item = ItemToPurchase(*args)
                func(item)

            else:
                func()

def terminal_input():
    ''' Interface with the user via the terminal by containing the control loop
        calling handle_command when the user provides input
    '''
    print("Shopping Cart")
    
    customer_name = input("Customer Name: ")
    todays_date = input("Today's Date: ")

    shopping_cart = ShoppingCart(customer_name, todays_date)

    print('Usage: option "Item_Name" Item_Price Item_quantity "Item_Description(optional)"')
    print_menu()

    while True:
        command = input("Choose an option: ")
        if handle_command(command, shopping_cart) == 'q':
            break


if __name__ == '__main__':
    terminal_input()