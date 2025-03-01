// ============================================================================
//                                sort_item.h
// Programmed by: Daniel Chen
// Date Created: 2/28/2025
// Purpose: Sort items
// ============================================================================

#ifndef SORT_ITEM_H
#define SORT_ITEM_H

#include <vector>
#include "itemClass.h"

using namespace std;


// Function to sort items by price
vector<Item> sortItemsByPrice(vector<Item>& items);

// Function to sort items by price (ascending order)
vector<Item> sortItemsByPrice_asc(vector<Item>& items);

// Function to sort items by name (alphabetical order)
vector<Item> sortItemsByitemName(vector<Item>& items);

// Function to sort items by name (reverse order)
vector<Item> sortItemsByitemName_asc(vector<Item>& items);


#endif