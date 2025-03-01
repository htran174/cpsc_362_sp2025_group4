// ============================================================================
//                                search_item.cpp
// Programmed by: Daniel Chen
// Date Created: 2/28/2025
// Purpose: Search items
// ============================================================================

#include <iostream>
#include <vector>
#include "search_item.h"

using namespace std;


// Function to search items by name
vector<Item> search_items_by_name(vector<Item>& items, string search)
{
    vector<Item> search_results; // Vector to store search results
    for(int i = 0; i < items.size(); i++)
    {
        if(items[i].getName() == search) // Check if name matches search
        {
            //Appends the item to the new vector
            search_results.push_back(items[i]);
        }
    }
    //returns the new vector
    return search_results;
}

// Function to search items by ID
vector<Item> search_items_by_ID(vector<Item>& items, int search)
{
    vector<Item> search_results; // Vector to store search results
    for(int i = 0; i < items.size(); i++)
    {
        if(items[i].getID() == search) // Check if item ID matches search
        {
            //Appends the item to the new vector
            search_results.push_back(items[i]);
        }
    }
    //returns the new vector
    return search_results;
}