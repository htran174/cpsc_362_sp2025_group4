// ============================================================================
//                                sort_item.cpp
// Programmed by: Daniel Chen
// Date Created: 2/28/2025
// Purpose: Sort items
// ============================================================================

#include "sort_item.h"

using namespace std;


// Function to sort items by price
vector<Item> sortItemsByPrice(vector<Item>& items)
{
    for(int i = 0; i < items.size(); i++)
    {
        for(int j = 0; j < items.size() - 1; j++)
        {
            if(items[j].getPrice() < items[j+1].getPrice())
            {
                swap(items[j], items[j+1]);
            }
        }
    }
    //returns the sorted vector
    return items;

}

// Function to compare items by price (ascending order)
vector<Item> sortItemsByPrice_asc(vector<Item>& items)
{
    for(int i = 0; i < items.size(); i++)
    {
        for(int j = 0; j < items.size() - 1; j++)
        {
            if(items[j].getPrice() > items[j+1].getPrice())
            {
                swap(items[j], items[j+1]);
            }
        }
    }
    //returns the sorted vector
    return items;
}

// Function to compare items by name (alphabetical order)
vector<Item> sortItemsByitemName(vector<Item>& items)
{
    for(int i = 0; i < items.size(); i++)
    {
        for(int j = 0; j < items.size() - 1; j++)
        {
            if(items[j].getName() > items[j+1].getName())
            {
                swap(items[j], items[j+1]);
            }
        }
    }
    //returns the sorted vector
    return items;
}

// Function to compare items by name (reverse order)
vector<Item> sortItemsByitemName_asc(vector<Item>& items)
{
    for(int i = 0; i < items.size(); i++)
    {
        for(int j = 0; j < items.size() - 1; j++)
        {
            if(items[j].getName() < items[j+1].getName())
            {
                swap(items[j], items[j+1]);
            }
        }
    }
    //returns the sorted vector
    return items;
}
