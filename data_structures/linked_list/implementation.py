# LinkedList: A doubly-linked list.
# Max Halpern



class LinkedList:      

    def __init__(self, node_value=None):
        """
        Initalize the double linked list.
        """
        self.value = node_value
        self.next = self
        self.prev = self
        self.length = 0

    def __str__(self, sb=[], cur=None):        
        if self.is_empty():
            return "[]"
        if self.is_last():
            return f'{self.value}]'
        if self.is_sentinel():
            return f"[{self.next.__str__()}"
        return f'{self.value} -> {self.next.__str__()}'

            

    def is_sentinel(self)-> bool:
        """
        Check to see if the list has a 
        sentinel node.

        returns True if the value is None
                False if the value is not None
        """
        return self.value == None
        
    def last(self):
        """
        Check to see if the last node of an empty lsit
        is the senitnel node itself.

        return the last node in the structure.
        """
        #check if self is the last before traversing.
        if self.is_last():
            return self
        #traverse through the list 
        cur = self
        while cur.next.value != None:
            cur = cur.next
        return cur
        

    def is_empty(self)-> bool:
        """
        Check if the list structure contains any nodes.

        returns True is the list is empty.
                False if the list is not empty.
        """
        if self.prev == self and self.next == self and self.is_sentinel():
            return True
        else:
            return False

    def is_last(self)-> bool:
        """
        Check the structure to see if the next value 
        is the sentinel node, thus being the end.

        return True if end of list False if not.
        """
        
        if self.next.value == None:
            return True
        else:
            return False

    def append(self, item)-> None:
        """
        Add data to the end of the structure if the list has 
        more than one node in it besides it sentinel node.

        Use the last node in the list, point its next pointer at 
        the new node. Then point the new nodes next pointer at the Senitnel
        node, and its previous pointer at the Last node. Finally, set the sentinels
        previous node to the newly added node.

        params item The linked list object itself with the data.
        """
        if self.next.value == None:
            self.append_to_head(item)
        else:
            last_node = self.prev
            last_node.next = item
            item.next = self
            self.prev = item
            item.prev = last_node                 
        
        
    def append_to_head(self, item)-> None:
        """
        Add data to the begining of the structure.

        params item The linked list object itself with the data.
        """
        self.prev = item
        self.next = item
        item.next = self
        item.prev = self
            
        
    def delete(self)-> None:
        """
        Reposition the nodes previous and next node
        to point at eachother, orphaning the current node.
        """
        front_node = self.prev
        back_node = self.next
        front_node.next = back_node
        back_node.prev = front_node
        
        
    def insert(self, item)-> None:
        """
        Insert an item into the list structure.

        params item The node to be inserted.
        """
        next_node = self.next
        next_node.prev = item
        item.next = next_node
        item.prev = self
        self.next = item

    def at(self, index: int):
        """
        Return the node at the given index.

        params index Int the index of the given node.

        returns Node at given index.
        """
        counter = 0
        while counter < index:
            self = self.next
            counter += 1
        return self

        
    def search(self, data):
        """
        Search the list for a particular value
        returing none if not in the list structure.

        params data The value to check against.

        returns Node with value or None if not in list.
        """     
        if self.value == None and data == None:
            return None
        while self.value != data or self.is_last():
            self = self.next
            if self.value == data:
                return self
            else:
                return None            


    def insert_before(self,data)-> None:
        """
        Insert data before an element in the list

        params data The Node to be inserted.
        """
        before_node = self.prev
        before_node.next = data
        data.prev = before_node
        data.next = self
        self.prev = data
        


    def insert_in_order(self, data):
        """
        Insert keeping order in the list.

        params data The node to be insetrted.
        
        """
        if self.is_sentinel() and self.is_last():
            self.append_to_head(data)
        elif self.value == None:
            #skip the sentinel
            self = self.next
            traverse = True
            while traverse:
                if self.value == None or self.value >= data.value:
                    self.insert_before(data)
                    traverse = False
                else:
                    self = self.next
