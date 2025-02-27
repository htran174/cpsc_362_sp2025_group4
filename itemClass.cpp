// ============================================================================
//                               itemClass.cpp
// ============================================================================
// Programmed by: Diego Borjas
// Date Created: 2/26/2025
// CSUF Software Engineering Class
// Professor Paul Oginni

#include "itemClass.h"

// =========================== Default Constructor =========================
Item::Item()
{
	itemName = "";
	description = "";
	seller = "";
	itemPrice = 0;
	shippingCost = 0;
	itemID = 0;
	stockQuantity = 0;
	inStock = false;
}
// ============================================================================

// ========================== Overloaded Constructor ==========================
Item::Item(string itemName, string description, string seller, double itemPrice, double shippingCost, int itemID, int stockQuantity, bool inStock)
{
	this->itemName = itemName;
	this->description = description;
	this->seller = seller;
	this->itemPrice = itemPrice;
	this->shippingCost = shippingCost;
	this->itemID = itemID;
	this->stockQuantity = stockQuantity;
	this->inStock = inStock;

}
// ============================================================================


// ============================================================================

// ================================ Destructor ================================
Item::~Item(){}
// ============================================================================

// =============================== setName method =============================
// INPUTS: The item name as a string for the parameter.
// ------
// OUTPUT: No output is returned nor produced.
// -------
// DESCRIPTION: This method will set the item object class' name into its
// respective variable location.
// ============================================================================
void Item::setName(string itemName)
{
	this->itemName = itemName;
}
// ============================================================================

// ========================== setDescription method ===========================
// INPUTS: The item description as a string for the parameter.
// ------
// OUTPUT: No output is returned nor produced.
// -------
// DESCRIPTION: This method will set the item's description into its respective
// variable location.
// ============================================================================
void Item::setDescription(string description)
{
	this->description = description;
}
// ============================================================================

// ============================== setSeller method ============================
// INPUTS: The seller who sells the item as a string.
// ------
// OUTPUT: No output is returned nor produced.
// -------
// DESCRIPTION: This method will set the seller's name or company which sells
// the respective item.
// ============================================================================
void Item::setSeller(string seller)
{
	this->seller = seller;
}
// ============================================================================

// =============================== setPrice method ============================
// INPUTS: The price number as an integer.
// ------
// OUTPUT: None.
// -------
// DESCRIPTION: This method will set the item's price and store it into its
// respective variable location.
// ============================================================================
void Item::setPrice(double itemPrice)
{
	this->itemPrice = itemPrice;
}
// ============================================================================

// ============================ setShipping method ============================
// INPUTS: The shipping costs amount as a double.
// ------
// OUTPUT: None.
// -------
// DESCRIPTION: This method will set the item's shipping costs and store it
// into its respective variable location, accounted for decimal prices.
// ============================================================================
void Item::setShipping(double shippingCost)
{
	this->shippingCost = shippingCost;
}
// ============================================================================

// ============================= setID method =================================
// INPUTS: The item's ID number as an integer.
// ------
// OUTPUT: None.
// -------
// DESCRIPTION: This method will set the item's ID number and store it
// into its respective variable location, for managing and tracking purposes.
// ============================================================================
void Item::setID(int itemID)
{
	this->itemID = itemID;
}
// ============================================================================

// ========================= setQuantity method ===============================
// INPUTS: The item's quantity in-stock as an integer.
// ------
// OUTPUT: None.
// -------
// DESCRIPTION: This method will set the item's quantity amount that is
// available on the store currently and and store it into its respective
// variable location.
// ============================================================================
void Item::setQuantity(int stockQuantity)
{
	this->stockQuantity = stockQuantity;
}
// ============================================================================

// ========================= setStock method ==================================
// INPUTS: The item's status whether it is in-stock or not as a boolean.
// ------
// OUTPUT: None.
// -------
// DESCRIPTION: This method will set the item's in-stock for managing purposes
// such as to check whether the item is available for purchase or not.
// ============================================================================
void Item::setStock(bool inStock)
{
	this->inStock = inStock;
}
// ============================================================================

// ========================= printName method ==================================
// INPUTS: None.
// ------
// OUTPUT: The item object class' name will be printed.
// -------
// DESCRIPTION: This method will print the item's name.
// ============================================================================
void Item::printName() const
{
	cout << itemName << endl;

	return;
}
// ============================================================================

// ======================== printDescription method ===========================
// INPUTS: None.
// ------
// OUTPUT: The item's description will be printed.
// -------
// DESCRIPTION: This method will print the item's description.
// ============================================================================
void Item::printDescription() const
{
	cout << description << endl;

	return;
}
// ============================================================================

// ========================== printSeller method ==============================
// INPUTS: None.
// ------
// OUTPUT: The item's seller will be printed.
// -------
// DESCRIPTION: This method will print the item's seller.
// ============================================================================
void Item::printSeller() const
{
	cout << seller << endl;

	return;
}
// ============================================================================

// ============================ getPrice method ===============================
// INPUTS: None.
// ------
// OUTPUT: The item's price will be returned back to main.
// -------
// DESCRIPTION: This method will return the item's price.
// ============================================================================
double Item::getPrice() const
{
	return itemPrice;
}
// ============================================================================

// ========================== getShipping method ==============================
// INPUTS: None.
// ------
// OUTPUT: The item's shipping costs will be returned back to main.
// -------
// DESCRIPTION: This method will return the item's shipping costs.
// ============================================================================
double Item::getShipping() const
{
	return shippingCost;
}
// ============================================================================

// ============================== getID method ================================
// INPUTS: None.
// ------
// OUTPUT: The item's ID number will be returned back to main.
// -------
// DESCRIPTION: This method will return the item's ID number.
// ============================================================================
int Item::getID() const
{
	return itemID;
}
// ============================================================================

// ========================== getQuantity method ==============================
// INPUTS: None.
// ------
// OUTPUT: The item's stock quantity will be returned back to main.
// -------
// DESCRIPTION: This method will return the item's stock quantity amount.
// ============================================================================
int Item::getQuantity() const
{
	return stockQuantity;
}
// ============================================================================

// =========================== checkStock method ==============================
// INPUTS: None.
// ------
// OUTPUT: The item's stock status will be returned back to main.
// -------
// DESCRIPTION: This method will return the item's stock status.
// ============================================================================
bool Item::checkStock() const
{
	return inStock;
}
// ============================================================================
