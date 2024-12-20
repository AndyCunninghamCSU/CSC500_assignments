# Andrew Cunningham
# CSC500 module 6 - portfolio milestone

'''
Step 6
attributes:
    customer name (string) = none
    current date (string) = Jan 1 2020
    cart items (list of items to purchase) = None

Methods
    add_item(item to purchase)
    remove_item(item to remove)
    modify_item (item to change)
    get_num_items_in_cart()
    get_cost_of_cart()
    print_total()
    print_descriptions()
'''

import ItemToPurchase
from ItemToPurchase import ItemToPurchase

class ShoppingCart:
    def __init__(self, customer_name: str, current_date='Jan 1 2020', list_of_items = None):
        '''customer_name = string
            current_date = string. Default = 'Jan 1 2020'
            list_of_items = list or ItemToPurchase

            Constructor does not type check, an invalid list of Items to Purchase might throw an error later.
        
        '''
        self.customer_name = customer_name
        self.current_date = current_date
        self.shopping_cart = list_of_items if list_of_items is not None else []

    def item_in_cart(self, item_to_check: ItemToPurchase):
        '''checks to see if item_to_check is valid -> True if in cart, False otherwise
        Raises typeError if item_to_check is not a valid ItemToPurchase
        '''
        if not isinstance(item_to_check, ItemToPurchase):
            raise TypeError(f"{item_to_check} is not a valid ItemToPurchase - NOT addedd to shopping card")

        return any(item.item_name == item_to_check.item_name for item in self.shopping_cart)

    def add_item(self, item: ItemToPurchase):
        '''Adds item to shopping_cart -> None'''

        if self.item_in_cart(item):
            print(f"Oops, {item.item_name} is already in the cart! do you instead want to call modify?")
            return

        self.shopping_cart.append(item)

    def remove_item(self, item: ItemToPurchase):
        '''Removes ItemToPurchase -> None
        outputs to console if item isn't found
        '''
        if not self.item_in_cart(item):
            print(f"{item.item_name} not found in cart. Nothing removed.")

        # shallow copy the shopping cart to enforce good practices
        for curr_item in self.shopping_cart[:]:
            if curr_item.item_name == item.item_name:
                self.shopping_cart.remove(curr_item)
                break

    def modify_item(self, item: ItemToPurchase):
        '''if the item current in the cart has a default price, quantity, or description, updates
        with args. -> nothing
        outputs and does nothing if item cannot be found
        '''
        if not self.item_in_cart(item):
            print(f"{item.item_name} not found in cart. Nothing modified.")

        for curr_item in self.shopping_cart[:]:
            if curr_item.item_name == item.item_name:
                if curr_item.has_default_quantity():
                    curr_item.item_quantity = item.item_quantity
                if curr_item.has_default_price():
                    curr_item.item_price = item.item_price
                if curr_item.has_default_description():
                    curr_item.item_description = item.item_description
                break

    def get_num_items_in_cart(self):
        '''returns count of all quantities'''
        count = 0
        for item in self.shopping_cart:
            count += item.item_quantity
        
        return count

    def get_cost_of_cart(self):
        '''returns total cost of all items in cart as float'''
        total = 0.0
        for item in self.shopping_cart:
            total += item.item_price * item.item_quantity

        return total

    def print_total(self):
        '''outputs total to console -> nothing'''
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        for item in self.shopping_cart:
            print(item.get_item_summary())
        print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        '''outputs shopping cart to console -> nothing'''
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.shopping_cart:
            print(item.get_item_description())
        

