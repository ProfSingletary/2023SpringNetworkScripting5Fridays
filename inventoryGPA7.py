#!/usr/bin/env python3

# inventoryGPA7.py
# 02/20/2022
# tests product class

from product import Product

def main():
    # create two product objects
    # edit the Product argument to include an amount for quantity
    product1 = Product("Stanley 13 Ounce Wood Hammer", 11.25, 62) # calls constructor
    product2 = Product('National Hardware 3/4" Wire Nails', 5.06, 0) # calls constructor

    # print data for product1 to console
    print("PRODUCT 1:")
    print("Name:\t\t\t{:s}".format(product1.name))
    print("Price:\t\t\t{:.2f}".format(product1.price))
    print("Discount percent:\t{:d}%".format(product1.discountPercent))
    print("Discount amount:\t{:.2f}".format(product1.getDiscountAmount()))
    print("Discount price:\t\t{:.2f}".format(product1.getDiscountPrice()))
    #print the quantity
    #print the total cost
    
    print() # blank line
    
    # print data for product2 to console
    print("PRODUCT 2:")
    print("Name:\t\t\t{:s}".format(product2.name))
    print("Price:\t\t\t{:.2f}".format(product2.price))
    print("Discount percent:\t{:d}%".format(product2.discountPercent))
    print("Discount amount:\t{:.2f}".format(product2.getDiscountAmount()))
    print("Discount price:\t\t{:.2f}".format(product2.getDiscountPrice()))
    #print the quantity
    #print the total cost

if __name__ == "__main__":
    main()
