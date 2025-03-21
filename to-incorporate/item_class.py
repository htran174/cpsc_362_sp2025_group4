"""
Programmer: Diego Borjas
Professor: Paul Oginni
Class: Software Engineering CPSC 362
Date: 20 March 2025
Group: #4
==================================================================
Description:
The Item class will represent and create every product that will be
available for purchase in the website's catalog. Each item will have its
name, description of item, the company that sells it, its price, unique ID
for managing purposes, stock quantity available in website to sell, and a
stock status variable to check whether it is out-of-stock or not.
===================================================================
"""

class Item:
    def __init__(self, itemName="", description="", seller="", itemPrice=0.0, shippingCost=0.0, itemID=0, stockQuantity=0, inStock=False):
        self.itemName = itemName
        self.description = description
        self.seller = seller
        self.itemPrice = itemPrice
        self.shippingCost = shippingCost
        self.itemID = itemID
        self.stockQuantity = stockQuantity
        self.inStock = inStock

    # sets the item's name.
    def setName(self, itemName):
        self.itemName = itemName
        
    # sets the item's description.
    def setDescription(self, description):
        self.description = description

    # sets the name of the person or company that sells the item.
    def setSeller(self, seller):
        self.seller = seller

    # sets the item's total price.
    def setPrice(self, itemPrice):
        self.itemPrice = itemPrice

    # sets the total cost of shipping for the item.
    def setShipping(self, shippingCost):
        self.shippingCost = shippingCost

    # sets the item's ID for managing purposes. 
    def setID(self, itemID):
        self.itemID = itemID

    # sets the quantity available in-stock of the item.
    def setQuantity(self, stockQuantity):
        self.stockQuantity = stockQuantity

    # sets whether the item is in-stock or not as a boolean.
    def setStock(self, inStock):
        self.inStock = inStock

    # Retrieves the item's name. 
    def getName(self):
        return self.itemName

    # Retrieves the item's description.
    def getDescription(self):
        return self.description

    # Retrieves the seller of item.
    def getSeller(self):
        return self.seller

    # Retrieves the total price of the item.
    def getPrice(self):
        return self.itemPrice

    # Retrieves the total shipping costs of the item.
    def getShipping(self):
        return self.shippingCost

    # Retrieves the item's ID number.
    def getID(self):
        return self.itemID

    # Retrieves the total quantity amount of stock available of the item.
    def getQuantity(self):
        return self.stockQuantity

    # Returns true or false depending whether the item's is available in-stock within the shop. 
    def checkStock(self):
        return self.inStock