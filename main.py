'''
Portfolio Project: Option 1, Online Shopping Cart 

Written by Md Rob, 3 September 2021 

This file contains the driver functions and code or ShoppingCart and ItemToPurchase class.
'''

def print_menu(ShoppingCart):
    
    user_input = ''
    
    while (user_input != "q"): #why Q doesn't work? or (user_input != "Q")
        
        print("      MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        user_input = str(input("Choose an option: "))
        
        if (user_input == "a") or (user_input == "A"):
            add_item_cart(ShoppingCart)
        elif (user_input == "r") or (user_input is "R"):
            remove_item_cart(ShoppingCart)
        elif (user_input == "c") or (user_input is "C"):
            if (ShoppingCart.get_num_items_in_cart() != 0):
                for row, col in enumerate(ShoppingCart.cart_items):
                    print("{} {} @ ${:0.2f} = ${:0.2f} ".format(ShoppingCart.cart_items[row][0], ShoppingCart.cart_items[row][1], ShoppingCart.cart_items[row][2], ShoppingCart.cart_items[row][1] * ShoppingCart.cart_items[row][2] ))
                item_name = str(input("What item do you like to change? "))
                change_item_cart(ShoppingCart, item_name) 
            else: print("Sorry, ShoppingCart is EMPTY")
        elif (user_input == "i") or (user_input is "I"):
            output_items_description(ShoppingCart)
        elif (user_input == "o") or (user_input is "O"):
            output_shopping_cart_menu(ShoppingCart)
        elif (user_input == "q"):
            print("MENU Exited, Good Bye!")
        else:
            print("OOPPS, Choose from the menu, please!")

def output_items_description(ShoppingCart):
    ShoppingCart.print_descriptions()

def change_item_cart(ShoppingCart, item_name):
    ShoppingCart.modify_item(ShoppingCart, item_name)
    
def output_shopping_cart_menu(ShoppingCart):
    print("OUTPUT SHOPPING CART")
    ShoppingCart.print_total()

def add_item_cart(ShoppingCart):
    print("What do you want to add?")
    item_1_name = str(input("Enter the item name: "))
    item_1_price = float(input("Enter the item price: "))
    item_1_quantity = int(input("Enter the item quantity: "))
    item_1_description = str(input("Enter an item descriptions: "))
    
    if item_1_description == "":
        print("Please enter {} descriptions.".format(item_1_name))
        item_1_description = str(input("Enter an item descriptions: "))
    
    item_1 = ItemToPurchase(item_1_name, item_1_quantity, item_1_price, item_1_description)
    ShoppingCart.add_item(item_1)
    print("***ITEM ADDED TO CART***")

def remove_item_cart(ShoppingCart):
    
    if (ShoppingCart.get_num_items_in_cart() != 0):
        print("***Remove item from carts***")
        ShoppingCart.show_cart_items()
        item_name = str(input("Enter an item to delete: "))
        ShoppingCart.remove_item(item_name)
    else: 
        print("ShoppingCart is EMPTY")

def main():
    
    print("Enter customer's name:")
    customer_name = str(input())
    
    while (customer_name.isdigit()):
        print("Name can't be digits, Enter customer's name: ")
        customer_name = str(input())
    
    print("Enter today's date (Month day, year): ")
    todays_date = str(input())
    
    print("Customer's name: {}".format(customer_name) )
    print("Today's date: {}".format(todays_date) )
    
    shoppingcart = ShoppingCart(customer_name, todays_date)
    print_menu(shoppingcart)
    
if __name__== "__main__":
    main()