// ============================================================================
//                                itemClass.h
// ============================================================================
// Programmed by: Diego Borjas
// Date Created: 2/25/2025
// CSUF Software Engineering Class
// Professor Paul Oginni

#ifndef ITEMCLASS_H
#define ITEMCLASS_H

#include <string>
#include <iomanip>
#include <iostream>

using namespace std;

/*****************************************************************************
 * itemClass.h object class
 * -------------------
 * The item class will represent and create every product that will be
 * available for purchase in the website's catalog. Each item will have its
 * name, description of item, the company that sells it, its price, unique ID
 * for managing purposes, stock quantity available in website to sell, and a
 * stock status variable to check whether it is out-of-stock or not.
 *****************************************************************************/

class Item
{
private:
	string itemName;
	string description;
	string seller;
	double itemPrice;
	double shippingCost;
	int itemID;
	int stockQuantity;
	bool inStock;
public:
	Item();
	Item(string itemName, string description, string seller, double itemPrice, double shippingCost, int itemID, int stockQuantity, bool inStock);
	~Item();
	void setName(string itemName);
	void setDescription(string description);
	void setSeller(string seller);
	void setPrice(double itemPrice);
	void setShipping(double shippingCost);
	void setID(int itemID);
	void setQuantity(int stockQuantity);
	void setStock(bool inStock);
	void printName() const;
	void printDescription() const;
	void printSeller() const;
	double getPrice() const;
	double getShipping() const;
	int getID() const;
	int getQuantity() const;
	bool checkStock() const;
};

#endif
