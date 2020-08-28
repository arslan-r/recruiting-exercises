import unittest

from src import InventoryAllocator


class TestInventoryAllocator(unittest.TestCase):

    def test_iA1(self):
        # order shipped with one ware house
        order = {'apple': 1}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 1}}]
        result = [{'owd': {'apple': 1}}]
        self.assertEqual(InventoryAllocator.inventory_allocator(
            order, warehouse), result)

    def test_iA2(self):
        # Order should be shipped from the first warehouse, even if other warehouses have requested items
        order = {'apple': 1}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 1}},
                     {'name': 'notThis', 'inventory': {'apple': 1}}]
        result = [{'owd': {'apple': 1}}]
        self.assertEqual(InventoryAllocator.inventory_allocator(
            order, warehouse), result)

    def test_iA3(self):
        # Order should be broken up between multiple warehouses
        order = {'apple': 5, 'banana': 5}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 5, 'pear': 10}}, {
            'name': 'dm', 'inventory': {'banana': 5}}]
        result = [{'owd': {'apple': 5}}, {'dm': {'banana': 5}}]
        self.assertEqual(InventoryAllocator.inventory_allocator(
            order, warehouse), result)

    def test_iA4(self):
        # Order can be filled by splitting up items first, but also by a warehouse at the end of the list
        order = {'apple': 1, 'pear': 1}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 1}}, {
            'name': 'win', 'inventory': {'apple': 1, 'pear': 1}}]
        result = [{'win': {'apple': 1, 'pear': 1}}]
        self.assertEqual(InventoryAllocator.inventory_allocator(
            order, warehouse), result)

    def test_iA5(self):
        # Order cannot be filled. Should return an empty list
        order = {'apple': 1}
        warehouse = [{'name': 'owd', 'inventory': {'apple': 0}}]
        result = []
        self.assertEqual(InventoryAllocator.inventory_allocator(
            order, warehouse), result)

    def test_iA6(self):
        # One warehouse should fill the order even if it is possible to split earlier
        order = {'apple': 5, 'banana': 5}
        warehouse = [{'name': 'hire', 'inventory': {'apple': 2, 'banana': 5}},
                     {'name': 'me', 'inventory': {'apple': 3}},
                     {'name': 'please', 'inventory': {'apple': 6}}]
        result = [{'hire': {'banana': 5}}, {'please': {'apple': 5}}]
        self.assertEqual(InventoryAllocator.inventory_allocator(
            order, warehouse), result)


if __name__ == '__main__':
    unittest.main()
