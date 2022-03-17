# Queue
# Max Halpern


from llist import sllist

class Queue:
    
    def __init__(self):
        self.items = 0
        self.data =  sllist()
        

    def enqueue(self,item):
        """
        Add an item to the rear of the queue then
        update the size of the queue.

        params: item ok hThe item to be added.
        """
        self.data.append(item)
        self.items += 1
        

    def dequeue(self):
        """
        Remove an item from the front queue then
        update the size of the queue.

        """
        if self.is_empty():
            raise ValueError("Queue is empty.")
            
        else:     
            self.items -= 1       
            return self.data.popleft()

    def is_empty(self)-> bool:
        """
        Check to see if the queue is empty.

        returns True if empty, False if not.
        """
        return self.data == sllist()

    def size(self)-> int:
        """
        Get the size of the queue.

        return int The size of the queue.
        """
        return self.items
