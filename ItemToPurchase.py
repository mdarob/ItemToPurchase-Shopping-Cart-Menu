'''
Portfolio Project: Option 1, Online Shopping Cart 

Written by Md Rob, 3 September 2021 

This is ItemToPurchase class that has two functions that calculates

item costs and total item costs.
'''

import numpy as np

class ItemToPurchase:
    
    item_name = "none"
    item_price = 0
    item_quantity = 0
    item_description = "none"

    def __init__(self, item_name, item_quantity, item_price, item_description):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        
        print("{} {} @ ${} = ${} ".format(self.item_name, self.item_quantity, self.item_price, self.item_quantity * self.item_price ))
        
    def total_cost(self):
        return self.item_quantity * self.item_price
