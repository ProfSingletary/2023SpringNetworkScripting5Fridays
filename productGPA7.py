#!/usr/bin/env python3
 
# productGPA7.py
# Class that represents a Product
 
class Product:
    # constructor
    # add a quantity member
    def __init__(self, name, price, discountPercent):
        # __ in front of the variable makes it 'read only' or private
        self.__name = name
        self.__price = price
        self.__discountPercent = discountPercent
 
    # accessor/setter for name using decorators
    @property
    def name(self):
        # print("in name getter") # debug
        return self.__name
 
    @name.setter
    def name(self, name):
        # print("in name setter, param=" + name) # debug
        if name == "":
            print("Error: name cannot be empty")
        else:
            self.__name = name
 
    # accessor/setter for price using decorators
    @property
    def price(self):
        # print("in price getter") # debug
        return self.__price
 
    @price.setter
    def price(self, price):
        # print("in price setter, param=" + str(price)) # debug
        if price < 0:
            print("Error: price cannot be negative")
        else:
            self.__price = price
 
    # accessor/setter for discountPercent using decorators
    @property
    def discountPercent(self):
        # print("in discountPercent getter") # debug
        return self.__discountPercent
 
    @discountPercent.setter
    def discountPercent(self, discountPercent):
        # print("in discountPercent setter, param=" + str(discountPercent)) # debug
        if (discountPercent < 0.0 ):
            print("Error: discount percentage cannot be negative")
        elif (discountPercent > 100.0):
            print("Error: discount percentage cannot be greater than 100%")
        else:
            self.__discountPercent = discountPercent

    # accessor/setter for quantity using decorators


    
    # calculate discount amount (price * discount percentage)
    def getDiscountAmount(self):
        return self.__price * self.__discountPercent / 100
 
    # calculate discount price (price - discount amount)
    def getDiscountPrice(self):
        return self.__price - self.getDiscountAmount()

    # calculate total cost (discount price * quantity)
