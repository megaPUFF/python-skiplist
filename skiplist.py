import random

class Node:

    def __init__( self, data, level=None ):
        self.max_height = 3 # TODO remove
        self.data = data 
        if level is None:
            self.level = random.randint(0, self.max_height)
        else:
            self.level = level

        self.skiplist = [None] * (self.level + 1) # must be level + 1
        self.skipindex = [1] + ([0] * self.level)

    def __str__( self ):
        return "<Node>Data:" + str(self.data) + ", List:" + str(self.skiplist) \
                + ", Index:" + str(self.skipindex)


class SkipList:
    """ singly linked skiplist, ordered. assume no duplicates """
    count = 0

    def __init__( self, max_height=3 ):
        self.head = None
        self.max_height = max_height

    def insert( self, data, level=None ):
        self.count += 1

        # empty
        if self.head is None:
            new_node = Node(data, self.max_height)
            self.head = new_node
            return

        # first elt
        if self.head.data > data:
            new_node = Node(data, self.max_height)
            new_node.skiplist = [self.head] * (self.max_height + 1) # old head
            new_node.skipindex = [1] * (self.max_height + 1)
            self.head = new_node
            return

        new_node = Node(data, level)

        return self._insert_r( data, self.head, self.head.level, new_node )

    def _insert_r( self, data, node, level, new_node ):
        """level - current level, not the same as insert()"""
        if node.skiplist[level] is None or \
                node.skiplist[level].data > data:
            # drop a level on the same node
            if level <= new_node.level:
                new_node.skiplist[level] = node.skiplist[level]
                node.skiplist[level] = new_node

            if level == 0:
                return 1
            else:
                index = self._insert_r( data, node, level-1, new_node )
                if level > new_node.level:
                    node.skipindex[level] += 1
                else:
                    new_node.skipindex[level] = \
                            node.skipindex[level] - index + 1
                    node.skipindex[level] = index
                return index

        else:
            # move forward to the next node
            index = \
                self._insert_r(data, node.skiplist[level], level, new_node)
            return index + node.skipindex[level]

    def remove( self, data ):
        if self.head is None:
            return

        if self.head.data == data:
            if self.head.skiplist[0] is None:
                # now empty
                self.head = None

            else:
                # first elt to be removed, promote next elt to full height
                new_head = self.head.skiplist[0]
                new_head.skiplist.extend(self.head.skiplist[new_head.level+1:])
                new_head.skipindex.extend( \
                    [ x-1 for x in self.head.skipindex[new_head.level+1:] ])
                new_head.level = self.max_height
                self.head = new_head

            self.count -= 1
            return

        return self._remove_r_find( data, self.head, self.head.level )

    def _remove_r_find( self, data, node, level ):
        while node.skiplist[level] is None or \
                node.skiplist[level].data > data:
            node.skipindex[level] -= 1
            level -= 1
            if level < 0:
                return None

        if node.skiplist[level].data == data:
            # found our element, so now we delegate to _remove_r_clear
            found_node = node.skiplist[level]
            self.count -= 1
            return self._remove_r_clear( data, node, level, found_node )

        return self._remove_r_find( data, node.skiplist[level], level )

    def _remove_r_clear( self, data, node, level, found_node ):
        while node.skiplist[level] == found_node:
            node.skiplist[level] = found_node.skiplist[level]
            node.skipindex[level] = node.skipindex[level] + found_node.skipindex[level] - 1
            level -= 1
            if level < 0:
                return

        return self._remove_r_clear( data, node.skiplist[level], level, found_node )

    def get_at( self, index ):
        """returns the Node at index @index in this SkipList"""
        if index < 0:
            return None

        if self.count <= 0:
            return None

        if index == 0:
            return self.head

        return self._get_at_r( index, self.head, self.head.level, 0 )

    def _get_at_r( self, index, node, level, current_index ):
        if node.skiplist[level] is None or \
                current_index + node.skipindex[level] > index:
            # skip is no good or too far - drop a level
            if level == 0:
                return None
            return self._get_at_r( index, node, level-1, current_index )

        elif current_index + node.skipindex[level] == index:
            return node.skiplist[level]

        else:
            return self._get_at_r( index, node.skiplist[level], level, \
                    current_index+node.skipindex[level] )

    def find( self, data ):
        current_node = self.head
        current_level = self.head.level

        while (current_node is not None):
            if current_node.data == data:
                return data

            while current_node.skiplist[current_level] is None or \
                  current_node.skiplist[current_level].data > data:
                current_level -= 1
                if (current_level < 0):
                    return None

            current_node = current_node.skiplist[current_level]

    def find_r( self, data ):
        if self.head.data == data:
            return data

        return self._find_r( data, self.head, self.head.level )

    def _find_r( self, data, node, level ):
        while node.skiplist[level] is None or \
                node.skiplist[level].data > data:
            level -= 1
            if level < 0:
                return None

        if node.skiplist[level].data == data:
            return data

        else:
            return self._find_r( data, node.skiplist[level], level )

    def relevel( self ):
        for i in range (10):
            i

    def _get_level( self, x ):
        """x=0 will return max_height"""
# TODO need to implement max_height
        if x == 0:
            return self.max_height
        level = 0

        while x%2 == 0 and x > 0:
            x /= 2
            level += 1

        return level

    def __str__( self ):
        s = '['
        current_node = self.head

        while current_node is not None:
            s += str(current_node.data) + ','
            current_node = current_node.skiplist[0]

        return s[:-1] + ']'
