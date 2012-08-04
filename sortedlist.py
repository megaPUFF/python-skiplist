class Node:

    def __init__( self, data ):
        self.data = data 
        self.next = None


class SortedList:
    """ singly linked list, ordered. assume no duplicates """

    def __init__( self ):
        self.head = None
        self.tail = None

    def insert( self, data ):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # should be first elt
        elif data < self.head.data:
            new_node.next = self.head
            self.head = new_node

        # should be first elt
        elif data > self.tail.data:
            self.tail.next = new_node
            self.tail = new_node

        else:
            current_node = self.head

            while (current_node is not None):

                if current_node.next is None:
                    # insert as last
                    current_node.next = new_node
                    self.tail = new_node
                    return

                elif current_node.next.data > data:
                    # insert here
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return

                else:
                    # loop
                    current_node = current_node.next

    def remove( self, data ):
        if (self.head is None):
            return

        if (self.head.data == data):
            self.head = self.head.next
            # not strictly necessary if we test self.head first:
            if self.head is None: # list is now empty
                self.tail = None
            return

        prev = None
        current_node = self.head
        while (current_node is not None):
            if (current_node.data == data):
                prev.next = current_node.next
                if (current_node == self.tail):
                    self.tail = prev
                return

            prev = current_node
            current_node = current_node.next
