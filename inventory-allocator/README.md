## How to run the tests
```
$ cd path/to/src
$ python test_InventoryAllocator.py
```

## What is my approach?
The challange specifies that shipping from one warehouse is cheaper than shipping from multiple. Therefore, we should scan each warehouse to see if they are capable of filling the order completely, and if not, break up the order prioritizing cheaper warehouses. 

#### How would we do that?
We will have to scan through the entire list of warehouses. As we scan along, add ordered items to the "cart". If there is a warehouse that can fill the entire order all at once, we fill the order and we are done. Else, we check if the "cart" can fill the order, and then we are done. 

My original appreach to this problem involved scanning the warehouses to see if there is one to completely fill the order, and if not, scan the warehouses again, splitting the order. This approach iterates over the warehouses twice. 

After some thought, I traded run time for space. Using an additional dict/map, we scan through the warehouses ONCE, splitting up the order from the start. Even after the order is filled, we continue scanning the rest of the warehouses to see if one can fill the order completely. 






## Problem

The problem is compute the best way an order can be shipped (called shipments) given inventory across a set of warehouses (called inventory distribution). 

Your task is to implement a function that will to produce the cheapest shipment.

The first input will be an order: a map of items that are being ordered and how many of them are ordered. For example an order of apples, bananas and oranges of 5 units each will be 

`{ apple: 5, banana: 5, orange: 5 }`

The second input will be a list of object with warehouse name and inventory amounts (inventory distribution) for these items. For example, the inventory across two warehouses called owd and dm for apples, bananas and oranges could look like

`[ 
    {
    	name: owd,
    	inventory: { apple: 5, orange: 10 }
    }, 
    {
    	name: dm:,
    	inventory: { banana: 5, orange: 10 } 
    }
]`

You can assume that the list of warehouses is pre-sorted based on cost. The first warehouse will be less expensive to ship from than the second warehouse.

You can use any language of your choice to write the solution (internally we use Typescript/Javascript, Python, and some Java). Please write unit tests with your code, a few are mentioned below, but these are not comprehensive. Fork the repository and put your solution inside of the src directory and include a way to run your tests!

## Examples

### Order can be shipped using one warehouse

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[{ owd: { apple: 1 } }]`

### Order can be shipped using multiple warehouses

Input: `{ apple: 10 }, [{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}]`  
Output: `[{ dm: { apple: 5 }}, { owd: { apple: 5 } }]`

### Order cannot be shipped because there is not enough inventory

Input: `{ apple: 1 }, [{ name: owd, inventory: { apple: 0 } }]`  
Output: `[]`

Input: `{ apple: 2 }, [{ name: owd, inventory: { apple: 1 } }]`  
Output: `[]`

## FAQs
**If an order can be completely shipped from one warehouse or shipped from multiple warehouses, which option is cheaper?**
  We can assume that shipping out of one warehouse is cheaper than shipping from multiple warehouses.

## What are we looking for

We'll evaluate your code via the following guidelines in no particular order:

1. **Readability**: naming, spacing, consistency
2. **Correctness**: is the solution correct and does it solve the problem
1. **Test Code Quality**: Is the test code comperehensive and covering all cases.
1. **Tool/Language mastery**: is the code using up to date syntax and techniques. 
