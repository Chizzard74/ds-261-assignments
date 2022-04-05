# BinarySearchTree: A binary search tree.
# Max Halpern

class BinarySearchTree():
    
    def __init__(self,key=None, lc=None, rc=None, parent=None):
        self.key = key
        self.left = lc
        self.right = rc
        self.parent = parent

    def insert(self, node):
        """
        Insert a node into the bst.

        params node The node added into the tree.
        """
        if self.key == None and self.parent == None:
            self = node
        elif node.key <= self.key:
            if self.has_left_child():
                return self.left.insert(node)
            else:                
                self.left = node
                self.left.parent = self
        else:
            if self.has_right_child():
                return self.right.insert(node)
            else:                
                self.right = node
                self.right.parent = self           


    def search(self, key):
        """
        Search the structure for a key.

        returns the key if there, else None.
        """
        if self.key == key:
            return self
        elif key < self.key and self.has_left_child():
            return self.left.search(key)
        elif key > self.key and self.has_right_child():
            return self.right.search(key)
        else:
            print(f"Sorry {key} is not in the BST.")
            return None
    
    def reset_node_data(self, key=None, lc=None, rc=None):
        """
        Update the current nodes data and pointers.
        """
        self.key = key
        self.left = lc
        self.right = rc
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self

    def delete(self, key):
        """
        Delete a node in the tree with a given key.
        If the key does not exist, raise KeyError.

        params key The nodes key to be compared against.
        """  
        #if current nodes key < key, continue to ask for smaller value until it equals the key
        #if current nodes key > key, continue to ask for larger value until it equals the key              
        if key < self.key:
            if self.has_left_child():
                return self.left.delete(key)

        if key > self.key and self.has_right_child():
            return self.right.delete(key)

        #if the root has no children and the roots key equals the key, set root to None and return self.
        if self.is_root() and not self.has_any_children() and key == self.key:
            self = None
            return self
        #this checks the root with a tree of 1 level depth
        elif self.is_root() and key == self.key and self.has_any_children():
            if self.has_both_children():
                if not self.left.has_any_children() and not self.right.has_any_children():
                  self.left.parent = self.right
                  self.right.left = self.left
                  self = self.right                 
                  return self
                else:
                   #this checks the root with a tree larger than 1 level of depth
                   next = self.find_next_larger_node()
                   self.key = next.key
                   next.parent.left = None
            #if the node only has left child, become the left child -> set the left childs left child to None, set the left childs parent to None orphaning the left child entirely
            elif self.has_left_child():
                self = self.left
                self.left = None
                self.parent = None              
                return self
            #if the node only has a right child, become the right child -> set the right childs right child to None and the right childs parent to None orphaning the right child.
            else:
                self = self.right
                self.right = None
                self.parent = None
                return self
         #if the key is a leaf node and set the left or right node of its parent to None
        elif self.is_leaf() and key == self.key:
            if self.is_left_child():
                self.parent.left = None
            else:
                self.parent.right = None
         #if the node has any children, starting with the left -> check if its a left child, if so
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.left.parent = self.right
                    self.key = self.right.key
                    self.right = None
                    
                elif self.is_right_child():
                   if self.has_any_children():
                      if self.has_both_children():
                         next = self.find_next_larger_node()                         
                         self.key = next.key

                         if next.parent.left == next:
                            next.parent.left = None

                         if next.parent.right == next:
                            next.parent.right = None                        
                         return self.find_root()

                      if self.has_left_child():
                         self.left.parent = self.parent
                         self.key = self.left.key

            else:
                if self.is_left_child():
                    self.right.parent = self.parent
                    self.parent.left = self.right

                elif self.is_right_child():
                    self.right.parent = self.parent
                    self.parent.right = self.right

        return self.find_root()

    def find_root(self):
        """
        Return the root of the tree by checking parent nodes.
        """
        if self.parent:
            return self.parent.find_root()
        return self


    def find_next_larger_node(self):
        """
        Find the node that is next largest to the current node.
        """
        next_larger_node = None
        if self.has_right_child():
            next_larger_node = self.right.minimum()
        else:
            if self.parent:
                if self.is_left_child():
                    next_larger_node = self.parent
                else:
                    self.parent.right = None
                    next_larger_node = self.parent.find_next_larger_node()
                    self.parent.right = self
        return next_larger_node  

    def minimum(self):
        """
        Return the smallest left most value in the tree.
        """ 
        if not self.has_left_child(): 
            return self
        return self.left.minimum()

    def find_max(self):
        """
        Return the largest right most value in the tree
        """        
        if not self.has_right_child():
            return self
        return self.right.find_max()   



    def is_leaf(self)-> bool:
        """
        Checks to see if the node has any children

        returns True if so, False if not.
        """
        return not self.left and not self.right
                        
        
    def is_root(self)-> bool:
        """
        Check to see if the current node is the root.

        returns True if root node, False if not.
        """
        return not self.parent

    def has_any_children(self)-> bool:
        """
        Check to see if the current node has any children.

        returns True if left or right child exists, False if not.
        """
        if self.right or self.left:
            return True
        return False

    def has_both_children(self)-> bool:
        """
        Check to see if the current node has both children.

        returns True if left and right child exists, False if not.
        """
        if self.right and self.left:
            return True
        return False    
    
    def has_left_child(self)-> bool:
        """
        Check to see if the current node has a left child.

        returns True if self.left is not None, false if self.left is None.
        """
        if self.left:
            return True
        return False

    def has_right_child(self)-> bool:
        """
        Check to see if the current node has a rigt child.

        returns True if self.right is not None, false if self.right is None.
        """
        if self.right:
            return True
        return False

    def is_left_child(self)-> bool:
        """
        Check to see if the current node is a left child.

        returns True if self.parent.left is self, False if not.
        """
        if self.parent and self.parent.left == self:
            return True
        return False

    def is_right_child(self)-> bool:
        """
        Check to see if the current node is a right child.

        returns True if self.parent.right is self, False if not.
        """
        if self.parent and self.parent.right == self:
            return True
        return False

    def has_parent(self)-> bool:
        """
        Check to see if the current node has any parents.

        returns True if node has parent, False if not.
        """
        if self.parent:
            return True
        else:
            return False  

    def keys(self, type:str, result=None)-> list:
      """
      Perform a traversal based on the type.

      params type The type of traversal.
      returns list The numbers in the given order.
      """
      if result == None:
         result = []
      #Pre order traversal
      if type == "pre":
         if not self:
            return
         result.append(self.key)
         if self.left:
            self.left.keys(type, result)
         if self.right:
            self.right.keys(type, result)
      #In order traversal
      if type == "in":
         if not self:
            return 
         if self.left:
            self.left.keys(type, result)
         result.append(self.key)
         if self.right:
            self.right.keys(type, result)
      #Post order traversal
      if type == "post":         
         if not self:
            return                
         if self.left:
            self.left.keys(type, result)
         if self.right:
            self.right.keys(type, result)
         result.append(self.key)
      return result

   

