"""
Deliverr Challange
Author: Arslan Rakhmankulov
"""

def inventory_allocator(order, warehouses):
    """
    :param order: A map of items being ordered
    :param warehouses: A list of objects with warehouse names and inventory amounts
    :return: A list of objects with warehouse names and items they fulfilled.
    """

    """
    Check every warehouse if they have items in stock. 
    If any warehouse can partially fill the order, add the item to the "cart", and save the warehouse name
    Upon encountering a warehouse that can fill the order completely, return its values.
    Otherwise, after scanning all the warehouses, check if the "cart" has the items to fill an order
    If it does, return the warehouse and the partial order they filled. Otherwise, the order cant be filled
    """
    return_dict_builder = {}
    one_warehouse_dict = {}
    one_warehouse_list = []
    cart = {}
    filled_by = []
    order_copy = dict(order)

    # if inputs are null, or if the lists are empty, return an empty list
    if order is None or not order or warehouses is None or not warehouses:
        return filled_by

    for warehouse in warehouses:
        warehouse_items = {}
        order_from_one_wh = {}
        for item in order:
            if item not in warehouse['inventory']:
                continue
            if item not in cart:
                cart[item] = 0
            if cart[item] < order_copy[item]:
                # if our order is less than available inventory, lets grab what we can
                if order_copy[item] >= warehouse['inventory'][item]:
                    cart[item] += warehouse['inventory'][item]
                    order_copy[item] -= warehouse['inventory'][item]
                    warehouse_items[item] = warehouse['inventory'][item]
                    return_dict_builder[warehouse['name']] = warehouse_items
                else:
                    cart[item] += order_copy[item]
                    warehouse_items[item] = order_copy[item]
                    return_dict_builder[warehouse['name']] = warehouse_items

            # If we encounter a warehouse that can fill previously separated orders, lets go with this one instead
            if order[item] <= warehouse['inventory'][item]:
                cart[item] = order[item]
                order_from_one_wh[item] = order[item]
                for wh in list(return_dict_builder):
                    if item in return_dict_builder[wh]:
                        temp_copy = dict(warehouse_items)
                        return_dict_builder[wh].pop(item)
                        warehouse_items = temp_copy
                    if return_dict_builder[wh] == {}:
                        return_dict_builder.pop(wh)
                return_dict_builder[warehouse['name']] = order_from_one_wh

            # if we encounter a warehouse that can fill the ENTIRE order, we return that warehouse and items it fills.
            if order_from_one_wh == order:
                one_warehouse_dict[warehouse['name']] = order_from_one_wh
                one_warehouse_list.append(one_warehouse_dict)
                return one_warehouse_list

    # Verifying that we can ship our order
    if cart == order and return_dict_builder is not None:
        for key in return_dict_builder:
            new_dict = {key: return_dict_builder[key]}
            filled_by.append(new_dict)
        return filled_by
    else:
        return []
