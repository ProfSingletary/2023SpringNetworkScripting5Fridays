#!/usr/bin/env python3

# inventory2.py
# tests product class

from productv2 import Product

def main():
    # create two product objects
    product1 = Product("Stanley 13 Ounce Wood Hammer", 12.99, 62, 100) # calls constructor
    product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0, 3000) # calls constructor

    # print data for product1 to console
    print("PRODUCT 1:")
    print("Name:\t\t\t{:s}".format(product1.name))
    product1.price = 11.25
    

    print("Price:\t\t\t{:.2f}".format(product1.price))
    print("Discount percent:\t{:d}%".format(product1.discountPercent))
    print("Discount amount:\t{:.2f}".format(product1.getDiscountAmount()))
    print("Discount price:\t\t{:.2f}".format(product1.getDiscountPrice()))
    print("Quantity:\t\t{:d}".format(product1.quantity))
    print("Total Cost:\t\t${:.0f}".format(product1.getTotalCost()))
    
    print() # blank line
   
    # print data for product2 to console
    print("PRODUCT 2:")
    print("Name:\t\t\t{:s}".format(product2.name))
    print("Price:\t\t\t{:.2f}".format(product2.price))
    print("Discount percent:\t{:d}%".format(product2.discountPercent))
    print("Discount amount:\t{:.2f}".format(product2.getDiscountAmount()))
    print("Discount price:\t\t{:.2f}".format(product2.getDiscountPrice()))
    print("Quantity:\t\t{:d}".format(product2.quantity))
    print("Total Cost:\t\t${:.0f}".format(product2.getTotalCost()))
    
if __name__ == "__main__":
    main()
