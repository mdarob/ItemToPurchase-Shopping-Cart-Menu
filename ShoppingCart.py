'''
Portfolio Project: Option 1, Online Shopping Cart 

Written by Md Rob, 3 September 2021 

This is ShoppingCart class that interacts with ItemToPurchase and calculates

every other aspects of the Shopping Cart menu.
'''

class ShoppingCart(ItemToPurchase):
    
    def __init__(self, customer_name, current_date):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
    
    def add_item(self, ItemToPurchase):
        self.cart_items.append( [ ItemToPurchase.item_name, ItemToPurchase.item_quantity, ItemToPurchase.item_price, ItemToPurchase.item_description ] )
    
    def remove_item(self, item_name):
     
        np_array_list = np.array(self.cart_items)
        
        for row, col in enumerate(np_array_list):
            
            if item_name in col:
                np_array_list = np.delete(np_array_list, row, axis=0)
                self.cart_items = np.array(np_array_list).tolist()
                print("***Item removed from carts***")
                return
    
        print("Item not found in cart. Nothing removed.") 
        
    def is_item_found(self, item_name):
        for row, col in enumerate(self.cart_items):
            if item_name in col:
                return True
            else:
                return False
    
    def modify_item(self, ItemToPurchase, item_name ):
        
        for row, col in enumerate(self.cart_items):
            if item_name in col:
                if ItemToPurchase.item_description == "none": 
                    modified_item_description = str(input("Enter {} item description: ".format(item_name) ))
                    self.cart_items[row][-1] = modified_item_description
                
                if ItemToPurchase.item_quantity == 0:
                    modified_item_quantity = int(input("Enter {} item quantity: ".format(item_name) ))
                    self.cart_items[row][-2] = modified_item_quantity
                   
                if ItemToPurchase.item_price == 0:
                    modified_item_price = float(input("Enter {} item price: ".format(item_name) ))
                    self.cart_items[row][-3] = modified_item_price
                    
                if (ItemToPurchase.item_description != "none") and (ItemToPurchase.item_quantity != 0) and (ItemToPurchase.item_price != 0):
                    print("Item {} found but Nothing modified.".format(item_name))
                
        if self.is_item_found(item_name) == False:
            print("Item not found in cart. Nothing modified.")
        
    def get_num_items_in_cart(self):
        # Returns quantity of all items in cart. Has no parameters.
        total_item_in_carts = 0
        for row, col in enumerate(self.cart_items):
            total_item_in_carts = self.cart_items[row][-3] + total_item_in_carts
        return total_item_in_carts
    
    def get_cost_of_cart(self):
        # Determines and returns the total cost of items in cart. Has no parameters.
        total_item_cost = 0
        for row, col in enumerate(self.cart_items):
            total_item_cost += ( self.cart_items[row][-2] * self.cart_items[row][-3]) 
        return total_item_cost
    
    def print_total(self):
        if (self.get_num_items_in_cart() is 0):
            print("SHOPPING CART IS EMPTY")
            return
            
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date) )
        print("Number of Items: {}".format(self.get_num_items_in_cart()))
        
        for row, col in enumerate(self.cart_items):
            print("{} {} @ ${:0.2f} = ${:0.2f} ".format(self.cart_items[row][0], self.cart_items[row][1], self.cart_items[row][2], self.cart_items[row][1] * self.cart_items[row][2] ))
        
        print("Total: ${:0.2f}".format(self.get_cost_of_cart())) 
     
    def print_descriptions(self):
        if (self.get_num_items_in_cart() is 0):
            print("SHOPPING CART IS EMPTY, No description")
            return
        
        print("{}'s Shopping Cart - {}".format(self.customer_name, self.current_date) )
        print("Item Descriptions") #align middle
        
        for row, col in enumerate(self.cart_items):
            print("{}: {}".format(self.cart_items[row][0], self.cart_items[row][-1]))
               
    def show_cart_items(self):
        for row, col in enumerate(self.cart_items):
            print("{} {} @ ${:0.2f} = ${:0.2f} ".format(self.cart_items[row][0], self.cart_items[row][1], self.cart_items[row][2], self.cart_items[row][1] * self.cart_items[row][2] ))
        #print(self.cart_items)