# Andrew Cunningham
# CSC500 module 4 - porfolio milestone


# Contains two methods to satisfy requirements for the assignment
# shopping_cart_terminal() meets requirements
# shopping_cart_gui() adds layers of complexity for my own curiosity and
# exploration

import ItemToPurchase 
from ItemToPurchase import ItemToPurchase
import tkinter as tk

class ShoppingCart:

    def __init__(self):
        '''
        Defines an empty shopping cart
        '''
        self.shopping_cart = []

    def calculate_total(self):
        '''
        returns the total of all the item prices * quantities for each of the items
        in the shopping cart
        '''
        total = 0

        for item in self.shopping_cart:
            total += item.get_total()
        
        return round(float(total), 2)
    
    
    def shopping_cart_stringify(self):
        '''
        Returns a string formatter:
        *Item Name* *Quantity* @ $*price* = $*total*
        with each item seperated by a new line
        '''
        cart_string = ""
        cart_string = "\n".join(item.print_item_cost() for item in self.shopping_cart)
        return cart_string

    # Basic shopping cart command line method to satisfy Step 2 
    # Step 2: Get input
    def shopping_cart_terminal(self):
        

        print("2 Item shopping cart!!")

        for i in range(1,3,1):
            print(f'Item {i}')
            name = input('Enter the item name: ')
            price = input('Enter the item price: ')
            quantity = input('Enter the item quantity: ')

            new_item = ItemToPurchase(name, price, quantity)

            self.shopping_cart.append(new_item)

        # Step 3
        print('Total Cost')

        print(self.shopping_cart_stringify())

        print(f'Total: ${self.calculate_total():.2f}')

    # generates a UI that collects ItemsToPurchase with input fields and
    # buttons
    # returns an array of ItemsToPurchase
    def shopping_cart_gui(self):

        '''
        Runs a gui that the user can use to input as many items as needed
        Displays the results in the gui
        '''
        def update_item_input_number():
            '''
            Updates the Item Number at the top of the GUI
            '''
            next_number = len(self.shopping_cart) + 1
            item_number.config(text=f"Item {next_number}")

        def process_entry():
            '''
            Saves all of the entries as an item
            Adds the item to the shopping cart
            and clears the fields
            and updates the item number
            '''
            item_name = entry1.get()
            item_price = entry2.get()
            item_quantity = entry3.get()

            new_item = ItemToPurchase(item_name, item_price, item_quantity)

            self.shopping_cart.append(new_item)

            entry1.delete(0, tk.END)
            entry2.delete(0, tk.END)
            entry3.delete(0, tk.END)

            update_item_input_number()

        # callback for "Add Another" button
        def add_another():
            '''
            Button handler that just calls process_entry because we process an entry
            both here and onsubmit
            '''
            process_entry()
        
        # callback for "Submit" button
        def submit():
            '''
            processess the last item and displays the total
            '''
            process_entry()

            for entry in root.winfo_children():
                entry.destroy()
            
            item_list = 'TOTAL COST\n'
            item_list += self.shopping_cart_stringify()
            item_list += '\nTotal: $'
            item_list += str(self.calculate_total())

            list_box = tk.Text(root, height=10, width=50, wrap=tk.WORD)
            list_box.insert(tk.END, item_list)
            list_box.config(state=tk.DISABLED)
            list_box.pack(padx=10, pady=10)

            tk.Button(root, text="Exit", command=root.destroy).pack(pady=10)

        # UI Elements
        root = tk.Tk()
        root.title("Shopping Cart")

        # Item Number
        item_number = tk.Label(root, text="Item 1")
        item_number.grid(row=0, column=0, columnspan=2, pady=5)

        # Item Name label and entry
        tk.Label(root, text="Item Name: ").grid(row=1, column=0,padx=5, pady=5)
        entry1 = tk.Entry(root, width=30)
        entry1.grid(row = 1, column=1,padx=5,pady=5)

        # Item Price label and entry
        tk.Label(root, text="Item Price:").grid(row=2,column=0,padx=5,pady=5)
        entry2 = tk.Entry(root, width=30)
        entry2.grid(row=2,column=1,padx=5,pady=5)

        # Item Quantity label and entry
        tk.Label(root, text="Item Quantity:").grid(row=3,column=0,padx=5,pady=5)
        entry3 = tk.Entry(root, width=30)
        entry3.grid(row=3,column=1,padx=5,pady=5)

        # Frame for the buttons
        button_frame = tk.Frame(root)
        button_frame.grid(row=4, column=0, columnspan=2, pady=10)

        # Add another item
        tk.Button(button_frame, text="Add Another Item", command=add_another).pack(side=tk.LEFT, padx=10)

        # Submit
        tk.Button(button_frame, text="Submit", command=submit).pack(side=tk.LEFT, padx=10)

        root.mainloop()


    
    


