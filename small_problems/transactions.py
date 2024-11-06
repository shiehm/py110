"""
Write a function that takes two arguments, an inventory item ID and a list of transactions, 
and returns a list containing only the transactions for the specified inventory item.
"""

def transactions_for(txn_id, txns):
    return [txn for txn in txns if txn['id'] == txn_id]

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

print(transactions_for(101, transactions))

"""
Building on the previous exercise, write a function that returns True or False based 
on whether or not an inventory item (an ID number) is available. As before, the function 
takes two arguments: an item ID and a list of transactions. The function should return 
True only if the sum of the quantity values of the item's transactions is greater than zero. 
Notice that there is a movement property in each transaction object. A movement value of 
'out' will decrease the item's quantity.

You may (and should) use the transactions_for function from the previous exercise.
"""

def is_item_available(txn_id, txns):
    matching_txns = transactions_for(txn_id, txns)
    counter = 0
    for txn in matching_txns:
        if txn['movement'] == 'in':
            counter += txn['quantity']
        elif txn['movement'] == 'out':
            counter -= txn['quantity']
    return counter > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True

