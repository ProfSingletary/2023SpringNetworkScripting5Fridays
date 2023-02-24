#!/usr/bin/env python3

# productv2.py
# Represents a Product

class Product:
    # constructor
    def __init__(self, name, price, discountPercent, quantity):
        self.__name = name
        self.__price = price
        self.__discountPercent = discountPercent
        self.__quantity = quantity

    # accessor/setter for name using decorators
    @property
    def name(self):
        # print("in name getter") # debug
        return self.__name

    @name.setter
    def name(self, name):
        # print("in name setter, param=" + name) # debug
        if name == "":
            print("name cannot be empty")
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
            print("price cannot be negative")
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
            print("discount percentage cannot be negative")
        elif (discountPercent > 100.0):
            print("discount percentage cannot be greater than 100%")
        else:
            self.__discountPercent = discountPercent

    # accessor/setter for quantity using decorators
    @property
    def quantity(self):
        # print("in quantity getter") # debug
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        # print("in quantity setter, param=" + str(quantity)) #debug
        if (quantity < 0):
            print("quantity cannot be negative")
        else:
            self.__quantity = quantity

    # calculate discount amount (price * discount percentage)
    def getDiscountAmount(self):
        return self.__price * self.__discountPercent / 100

    # calculate discount price (price - discount amount)
    def getDiscountPrice(self):
        return self.__price - self.getDiscountAmount()

    #calculate total cost - quantity * discounted price
    def getTotalCost(self):
        return self.__quantity * self.getDiscountPrice()
