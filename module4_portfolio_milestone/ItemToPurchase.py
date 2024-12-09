# Andrew Cunningham
# CSC 500 Module 4 - Portfolio Milestone

# Step 1: Build the ItemToPurchase class with the following specifications:

# Attributes
#   item_name (string)
#   item_price (float)
#   item_quantity (int)
# Default constructor
#   Initializes item's name = "none", item's price = 0, item's quantity = 0
# Method
#   print_item_cost()

class ItemToPurchase:

    def __init__(self, item_name = 'none', item_price = 0.0, item_quantity = 0):
        '''
        Attempts to cleanse item_price and item_quantity
        item_name: String
        item_price: float with 2 signifigant figures.
        item_quantity: int
        '''
        self.item_name = item_name.strip() if item_name and item_name.strip() else 'none'
        self.item_price = self.clean_price(item_price)
        self.item_quantity = self.clean_int(item_quantity)

    @staticmethod
    def clean_price(raw_price):
        '''
        attempts to sanitize price by removing whitespace, $, and commas from the price
        returns a float with 2 decimals if successful
        returns 0.0 if fails for the default constructor
        '''
        try:

            cleaned = raw_price.strip()
            cleaned = cleaned.replace("$", "").replace(",","")

            return round(float(cleaned), 2)
        except:
            # An unknown error has occured with the cleaning operation
            return 0.0
    
    @staticmethod
    def clean_int(number):
        """
        Simple method to cast raw_quantity to an int and return a default "0" if an exception is raised.
        """
        try:
            return int(number)
        except:
            return 0

    def get_total(self):
        '''
        returns quantity * price as a float
        '''
        return self.item_quantity * self.item_price

    def print_item_cost(self):
        return f"{self.item_name} {self.item_quantity} @ ${self.item_price:.2f} = ${self.get_total():.2f}"
    
