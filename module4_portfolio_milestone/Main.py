# Andrew Cunningham
# CSC500 Module 4
# Porfolio Milestone

# Executes the shopping cart
# Can switch between terminal and GUI by updating boolean GUI_CART

from ShoppingCart import ShoppingCart

# True = GUI
# False = terminal
GUI_CART = False

cart = ShoppingCart()

if (GUI_CART):
    cart.shopping_cart_gui() 
else:
    cart.shopping_cart_terminal()




