import unittest

from sortedlist import Node
from sortedlist import SortedList

from random import shuffle

class TestSortedListFunctions(unittest.TestCase):

    def test_init_node_number(self):
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.next)

    def test_init_node_string(self):
        string = 'yet a string'
        node = Node(string)
        self.assertEqual(node.data, string)

    def test_init_SL(self):
        sl = SortedList()
        self.assertIsNone(sl.head)
        self.assertIsNone(sl.tail)

    def test_insert_first(self):
        sl = SortedList()
        sl.insert( 1 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.tail.data, 1)

    def test_insert_second(self):
        sl = SortedList()
        sl.insert( 2 )
        sl.insert( 1 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.next.data, 2)
        self.assertEqual(sl.tail.data, 2)
        self.assertIsNone(sl.tail.next)

    def test_insert_second_1(self):
        sl = SortedList()
        sl.insert( 1 )
        sl.insert( 2 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.next.data, 2)
        self.assertEqual(sl.tail.data, 2)
        self.assertIsNone(sl.tail.next)

    def test_insert_third(self):
        sl = SortedList()
        sl.insert( 3 )
        sl.insert( 2 )
        sl.insert( 1 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.next.data, 2)
        self.assertEqual(sl.head.next.next.data, 3)
        self.assertEqual(sl.tail.data, 3)
        self.assertIsNone(sl.tail.next)

    def test_insert_third_1(self):
        sl = SortedList()
        sl.insert( 1 )
        sl.insert( 2 )
        sl.insert( 3 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.next.data, 2)
        self.assertEqual(sl.head.next.next.data, 3)
        self.assertEqual(sl.tail.data, 3)
        self.assertIsNone(sl.tail.next)

    def test_remove(self):
        sl = SortedList()
        sl.insert( 1 )
        sl.remove( 1 )
        sl.remove( 1 )
        self.assertIsNone(sl.head)
        self.assertIsNone(sl.tail)

    def test_remove_first(self):
        sl = SortedList()
        sl.insert( 2 )
        sl.insert( 1 )

        sl.remove( 1 )

        self.assertEqual(sl.head.data, 2)
        self.assertEqual(sl.tail.data, 2)
        self.assertIsNone(sl.tail.next)

    def test_remove_last(self):
        sl = SortedList()
        sl.insert( 2 )
        sl.insert( 1 )

        sl.remove( 2 )

        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.tail.data, 1)
        self.assertIsNone(sl.tail.next)

    def test_remove_middle(self):
        sl = SortedList()
        sl.insert( 3 )
        sl.insert( 2 )
        sl.insert( 1 )

        sl.remove( 2 )

        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.next.data, 3)
        self.assertEqual(sl.tail.data, 3)
        self.assertIsNone(sl.tail.next)

    def test_stress(self):
        sl = SortedList()
        items = list( range(3000) )
        shuffle( items )
        for i in range(3000):
            sl.insert( items[i] )
            sl.remove( i / 2 )
            sl.remove( i / 3 )

if __name__ == '__main__':
    unittest.main()
