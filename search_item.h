// ============================================================================
//                                search_item.h
// Programmed by: Daniel Chen
// Date Created: 2/28/2025
// Purpose: Search items
// ============================================================================

#ifndef SEARCH_ITEM_H
#define SEARCH_ITEM_H

#include <vector>
#include "itemClass.h"

using namespace std;


// Function to search items by name
vector<Item> search_items_by_name(vector<Item>& items, string search);

// Function to search items by ID
vector<Item> search_items_by_ID(vector<Item>& items, int search);

#endif