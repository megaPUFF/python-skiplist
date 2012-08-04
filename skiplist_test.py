import unittest

from skiplist import Node
from skiplist import SkipList

from random import shuffle

class TestSkipListFunctions(unittest.TestCase):

    def test_init_node_number(self):
        node = Node(5)
        self.assertEqual(node.data, 5)
        self.assertIsNone(node.skiplist[0])

    def test_init_node_string(self):
        string = 'yet a string'
        node = Node(string)
        self.assertEqual(node.data, string)

    def test_init_SL(self):
        sl = SkipList()
        self.assertIsNone(sl.head)

    def test_get_at_1(self):
        sl = SkipList()

        self.assertIsNone(sl.get_at(0))
        self.assertIsNone(sl.get_at(1))

    def test_get_at_2(self):
        sl = SkipList()

        self.assertIsNone(sl.get_at(-1))

    def test_get_at_3(self):
        sl = SkipList()
        sl.insert( 1, 2 )
        sl.insert( 2, 0 )
        sl.insert( 3, 1 )

        self.assertEqual(sl.get_at(0).data, 1)
        self.assertEqual(sl.get_at(1).data, 2)
        self.assertEqual(sl.get_at(2).data, 3)
        self.assertIsNone(sl.get_at(3))

    def test_insert_r_first(self):
        sl = SkipList()
        sl.insert( 1 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.skiplist.count(None), sl.max_height+1)

    def test_insert_r_second_1(self):
        sl = SkipList()
        sl.insert( 2, 0 )
        sl.insert( 1, 0 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.skiplist[0].data, 2)
        self.assertEqual(sl.get_at(0).skiplist.count(None), 0)
        self.assertEqual(sl.get_at(1).skiplist.count(None), sl.max_height+1)

    def test_insert_r_second_2(self):
        sl = SkipList()
        sl.insert( 1, 0 )
        sl.insert( 2, 0 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.skiplist[0].data, 2)
        self.assertEqual(sl.get_at(0).skiplist.count(None), sl.max_height)
        self.assertEqual(sl.get_at(1).skiplist.count(None), 1)

    def test_insert_r_third_1(self):
        sl = SkipList()
        sl.insert( 3 )
        sl.insert( 2 )
        sl.insert( 1 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.skiplist[0].data, 2)
        self.assertEqual(sl.head.skiplist[0].skiplist[0].data, 3)
        self.assertEqual(sl.get_at(0).skiplist.count(None), 0)
        self.assertEqual(sl.get_at(1).skiplist.count(None), 0)
        self.assertEqual(sl.get_at(2).skiplist.count(None), sl.max_height+1)

    def test_insert_r_third_2(self):
        sl = SkipList()
        sl.insert( 1 )
        sl.insert( 2 )
        sl.insert( 3 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.skiplist[0].data, 2)
        self.assertEqual(sl.head.skiplist[0].skiplist[0].data, 3)

    def test_insert_r_third_3(self):
        sl = SkipList()
        sl.insert( 1 )
        sl.insert( 2, 1 )
        sl.insert( 3, 0 )
        self.assertEqual(sl.get_at(0).skiplist.count(None), sl.max_height-1)
        self.assertEqual(sl.get_at(1).skiplist.count(None), 1)
        self.assertEqual(sl.get_at(2).skiplist.count(None), 1)

    def test_insert_r_index_1(self):
        sl = SkipList()
        sl.insert( 1, sl.max_height )
        sl.insert( 2, 1 )
        sl.insert( 3, sl.max_height )
        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 1)
        self.assertEqual(sl.get_at(0).skipindex[2], 2)
        self.assertEqual(sl.get_at(0).skipindex[sl.max_height], 2)
        self.assertEqual(sl.get_at(1).skipindex[0], 1)
        self.assertEqual(sl.get_at(1).skipindex[1], 1)

    def test_insert_r_index_2(self):
        sl = SkipList()
        sl.insert( 1, sl.max_height )
        sl.insert( 2, 0 )
        sl.insert( 3, 1 )
        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 2)
        self.assertEqual(sl.get_at(1).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[0], 1)

    def test_insert_r_index_3(self):
        sl = SkipList()
        sl.insert( 1, sl.max_height )
        sl.insert( 2, 0 )
        sl.insert( 3, 1 )
        sl.insert( 4, 1 )
        sl.insert( 5, sl.max_height )

        self.assertEqual(sl.get_at(3).skipindex[0], 1)
        self.assertEqual(sl.get_at(3).skipindex[1], 1)
        self.assertEqual(sl.get_at(2).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[1], 1)
        self.assertEqual(sl.get_at(1).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 2)
        self.assertEqual(sl.get_at(0).skipindex[2], 4)
        self.assertEqual(sl.get_at(0).skipindex[sl.max_height], 4)

    def test_insert_r_index_4(self):
        # middle insert
        sl = SkipList()
        sl.insert( 1, sl.max_height )
        sl.insert( 2, 0 )
        sl.insert( 4, 1 )
        sl.insert( 5, sl.max_height )
        sl.insert( 3, 2 )

        self.assertEqual(sl.get_at(3).skipindex[0], 1)
        self.assertEqual(sl.get_at(3).skipindex[1], 1)
        # *****
        self.assertEqual(sl.get_at(2).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[1], 1)
        self.assertEqual(sl.get_at(2).skipindex[2], 2)
        # *****
        self.assertEqual(sl.get_at(1).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 2)
        self.assertEqual(sl.get_at(0).skipindex[2], 2)
        self.assertEqual(sl.get_at(0).skipindex[sl.max_height], 4)

    def test_insert_r_index_5(self):
        sl = SkipList()
        sl.insert( 1, sl.max_height )
        sl.insert( 5, sl.max_height )
        sl.insert( 2, 0 )
        sl.insert( 4, 1 )
        sl.insert( 3, 1 )

        self.assertEqual(sl.get_at(3).skipindex[0], 1)
        self.assertEqual(sl.get_at(3).skipindex[1], 1)
        self.assertEqual(sl.get_at(2).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[1], 1)
        self.assertEqual(sl.get_at(1).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 2)
        self.assertEqual(sl.get_at(0).skipindex[2], 4)
        self.assertEqual(sl.get_at(0).skipindex[sl.max_height], 4)

    def test_remove_r(self):
        sl = SkipList()
        sl.insert( 1 )
        sl.remove( 1 )
        sl.remove( 1 )
        self.assertIsNone(sl.head)

    def test_remove_r_first(self):
        sl = SkipList()
        sl.insert( 1 )
        sl.insert( 2, 0 )

        sl.remove( 1 )

        self.assertEqual(sl.head.data, 2)
        self.assertEqual(sl.head.level, sl.max_height)
        for i in range(sl.max_height+1):
            self.assertIsNone(sl.head.skiplist[i])

    def test_remove_r_last(self):
        sl = SkipList()
        sl.insert( 2 )
        sl.insert( 1 )

        sl.remove( 2 )

        self.assertEqual(sl.head.data, 1)
        for i in range(sl.max_height+1):
            self.assertIsNone(sl.head.skiplist[i])

    def test_remove_r_middle_1(self):
        sl = SkipList()
        sl.insert( 3 )
        sl.insert( 2 )
        sl.insert( 1 )

        sl.remove( 2 )

        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.get_at(1).data, 3)

        self.assertIsNone(sl.find(2))

        sl.insert( 2 )
        self.assertEqual(sl.get_at(1).data, 2)
        self.assertEqual(sl.get_at(2).data, 3)

    def test_remove_r_middle_2(self):
        sl = SkipList()
        sl.insert( 1, 3 )
        sl.insert( 2, 0 )
        sl.insert( 3, 0 )
        sl.insert( 4, 2 )
        sl.insert( 5, 0 )
        sl.insert( 6, 3 )

        sl.remove( 4 )

        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.get_at(0).skiplist[2].data, 6)
        self.assertEqual(sl.get_at(0).skiplist[1].data, 6)
        self.assertEqual(sl.get_at(2).skiplist[0].data, 5)

    def test_remove_r_index_1(self):
        sl = SkipList()
        sl.insert( 1, 2 )
        sl.insert( 2, 0 )
        sl.insert( 3, 1 )
        sl.insert( 4, 0 )
        sl.insert( 5, 2 )

        sl.remove( 3 )

        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 3)
        self.assertEqual(sl.get_at(0).skipindex[2], 3)

        self.assertEqual(sl.get_at(1).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[0], 1)

    def test_remove_r_index_2(self):
        sl = SkipList()
        sl.insert( 1, 3 )
        sl.insert( 2, 0 )
        sl.insert( 3, 1 )
        sl.insert( 4, 2 )
        sl.insert( 5, 3 )

        sl.remove( 3 )

        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 2)
        self.assertEqual(sl.get_at(0).skipindex[2], 2)
        self.assertEqual(sl.get_at(0).skipindex[3], 3)

        self.assertEqual(sl.get_at(1).skipindex[0], 1)

        self.assertEqual(sl.get_at(2).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[1], 1)
        self.assertEqual(sl.get_at(2).skipindex[2], 1)

    def test_remove_r_index_3(self):
        sl = SkipList()
        sl.insert( 1, 3 )
        sl.insert( 5, 3 )
        sl.insert( 2, 0 )
        sl.insert( 3, 1 )
        sl.insert( 4, 2 )

        sl.remove( 3 )

        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 2)
        self.assertEqual(sl.get_at(0).skipindex[2], 2)
        self.assertEqual(sl.get_at(0).skipindex[3], 3)

        self.assertEqual(sl.get_at(1).skipindex[0], 1)

        self.assertEqual(sl.get_at(2).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[1], 1)
        self.assertEqual(sl.get_at(2).skipindex[2], 1)

    def test_remove_r_index_4(self):
        # remove first
        sl = SkipList()
        sl.insert( 1, 3 )
        sl.insert( 2, 1 )
        sl.insert( 3, 0 )
        sl.insert( 4, 2 )
        sl.insert( 5, 3 )

        sl.remove( 1 )

        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 2)
        self.assertEqual(sl.get_at(0).skipindex[2], 2)
        self.assertEqual(sl.get_at(0).skipindex[3], 3)

        self.assertEqual(sl.get_at(1).skipindex[0], 1)

        self.assertEqual(sl.get_at(2).skipindex[0], 1)
        self.assertEqual(sl.get_at(2).skipindex[1], 1)
        self.assertEqual(sl.get_at(2).skipindex[2], 1)

    def test_remove_r_index_5(self):
        # remove last
        sl = SkipList()
        sl.insert( 1, 2 )
        sl.insert( 2, 1 )
        sl.insert( 3, 0 )
        sl.insert( 4, 2 )

        sl.remove( 4 )
        sl.insert( 4, 2 )

        self.assertEqual(sl.get_at(0).skipindex[0], 1)
        self.assertEqual(sl.get_at(0).skipindex[1], 1)
        self.assertEqual(sl.get_at(0).skipindex[2], 3)

        self.assertEqual(sl.get_at(1).skipindex[0], 1)
        self.assertEqual(sl.get_at(1).skipindex[1], 2)

        self.assertEqual(sl.get_at(2).skipindex[0], 1)

    def test_str(self):
        sl = SkipList()
        sl.insert( 3 )
        sl.insert( 2 )
        sl.insert( 1 )
        self.assertEqual(str(sl), '[1,2,3]')

    def test_skip_1(self):
        sl = SkipList()
        sl.insert( 3, 3 )
        sl.insert( 2, 1 )
        sl.insert( 1, 3 )
        self.assertEqual(sl.head.level, 3)
        self.assertEqual(sl.find(2), 2)
        self.assertEqual(sl.get_at(1).level, 3)
        self.assertEqual(sl.head.skiplist[0].data, 2)
        self.assertEqual(sl.head.skiplist[1].data, 2)

    def test_skip_2(self):
        sl = SkipList()
        sl.insert( 1, 1 )
        sl.insert( 2, 0 )
        sl.insert( 3, 1 )
        self.assertEqual(sl.head.data, 1)
        self.assertEqual(sl.head.skiplist[0].data, 2)
        self.assertEqual(sl.head.skiplist[1].data, 3)

    def test_find_1(self):
        sl = SkipList()
        sl.insert( 3, 0 )
        sl.insert( 1, 0 )

        self.assertEqual(sl.find(1), 1)

    def test_find_2(self):
        sl = SkipList()
        sl.insert( 3, 0 )
        sl.insert( 1, 0 )

        self.assertEqual(sl.find(1), 1)
        self.assertEqual(sl.find(3), 3)
        self.assertEqual(sl.find(2), None)

    def test_find_3(self):
        sl = SkipList()
        sl.insert( 3, 0 )
        sl.insert( 2, 0 )
        sl.insert( 1, 1 )

        self.assertEqual(sl.find(1), 1)
        self.assertEqual(sl.find(2), 2)
        self.assertEqual(sl.find(3), 3)
        self.assertEqual(sl.find(4), None)

    def test_find_4(self):
        sl = SkipList()
        sl.insert( 3, 1 )
        sl.insert( 2, 0 )
        sl.insert( 1, 1 )

        self.assertEqual(sl.find(1), 1)
        self.assertEqual(sl.find(2), 2)
        self.assertEqual(sl.find(3), 3)
        self.assertEqual(sl.find(1.5), None)


    def test_find_r_1(self):
        sl = SkipList()
        sl.insert( 3, 0 )
        sl.insert( 1, 0 )

        self.assertEqual(sl.find_r(1), 1)

    def test_find_r_2(self):
        sl = SkipList()
        sl.insert( 3, 0 )
        sl.insert( 1, 0 )

        self.assertEqual(sl.find_r(1), 1)
        self.assertEqual(sl.find_r(3), 3)
        self.assertEqual(sl.find_r(2), None)

    def test_find_r_3(self):
        sl = SkipList()
        sl.insert( 3, 0 )
        sl.insert( 2, 0 )
        sl.insert( 1, 1 )

        self.assertEqual(sl.find_r(1), 1)
        self.assertEqual(sl.find_r(2), 2)
        self.assertEqual(sl.find_r(3), 3)
        self.assertEqual(sl.find_r(4), None)

    def test_find_r_4(self):
        sl = SkipList()
        sl.insert( 3 )
        sl.insert( 2 )
        sl.insert( 1 )

        self.assertEqual(sl.find_r(1), 1)
        self.assertEqual(sl.find_r(2), 2)
        self.assertEqual(sl.find_r(3), 3)
        self.assertEqual(sl.find_r(1.5), None)

    def test_stress(self):
        limit = 3000
        sl = SkipList()
        items = list( range(limit) )
        shuffle( items )
        for i in range(limit):
            sl.insert( items[i] )
            sl.remove( i / 2 )

    def test__get_level(self):
        sl = SkipList(15)

        for x in range(1, 101, 2):
            self.assertEqual(sl._get_level(x), 0)

        self.assertEqual(sl._get_level(0), sl.max_height)
        self.assertEqual(sl._get_level(2), 1)
        self.assertEqual(sl._get_level(4), 2)
        self.assertEqual(sl._get_level(6), 1)
        self.assertEqual(sl._get_level(8), 3)
        self.assertEqual(sl._get_level(10), 1)
        self.assertEqual(sl._get_level(12), 2)
        self.assertEqual(sl._get_level(14), 1)
        self.assertEqual(sl._get_level(16), 4)

    def test__get_level(self):
        sl = SkipList(3)

        for x in range(1, 101, 2):
            self.assertEqual(sl._get_level(x), 0)

        self.assertEqual(sl._get_level(0), sl.max_height)
        self.assertEqual(sl._get_level(2), 1)
        self.assertEqual(sl._get_level(4), 2)
        self.assertEqual(sl._get_level(6), 1)
        self.assertEqual(sl._get_level(8), 3)
        self.assertEqual(sl._get_level(10), 1)
        self.assertEqual(sl._get_level(12), 2)
        self.assertEqual(sl._get_level(14), 1)
        self.assertEqual(sl._get_level(16), 3)

    def test_relevel(self):
        sl = SkipList()

if __name__ == '__main__':
    unittest.main()
