# Deque: A deque.
# Max Halpern

import llist
from llist import dllist

class Deque:
    
    def __init__(self):
        self.items = 0
        self.data = dllist()

    def enqueue_left(self,item):
        """
        Add an item to the left side of the deque then 
        update the size of the deque.

        params item The item to be added.
        """
        self.data.appendleft(item)
        self.items += 1

    def enqueue_right(self,item):
        """
        Add an item to the right side of the deque then 
        update the size of the deque.

        params item The item to be added.
        """
        self.data.appendright(item)
        self.items += 1

    def is_empty(self)-> bool:
        """
        Check to see if the deque is empty or not.

        returns True if empty, False if not.
        """
        return self.data == dllist()

    def dequeue_left(self):
        """
        Return the left most value in the deque.

        returns Left most element in deque if not empty.
        """
        if not self.is_empty():
            self.items -= 1
            return self.data.popleft()
        raise ValueError("Empty deque.")

    def dequeue_right(self):
        """
        Return the right most value in the deque.

        returns Right most element in deque if not empty.
        """
        if not self.is_empty():
            self.items -= 1
            return self.data.pop()
        raise ValueError("Empty deque.")

    def size(self)-> int:
        """
        Return the size of the deque.

        returns int The size of the deque.
        """
        return self.items

    