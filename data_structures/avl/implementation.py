# AVLTree: A Self-balancing Binary Search Tree
# Max Halpern

class AVLTree:

    def __init__(self, key=None, left=None, right=None, parent=None, balance_factor=0) -> None:
        self.left = left
        self.right = right
        self.key = key
        self.parent = parent
        self.balance_factor = balance_factor

    # #Add additional methods as needed. Use the helper methods provided below.


    def get_left_height(self,node, l_height = 0) -> int:
        """
        Gets the height of the left subtree of a current node.

        params node: The current node we are on
               l_height: to start, 0 is the value of the left subtree
               then we add one to the counter for each child.

        returns Int the height of the left subtree.
        """       
        if node.left:
            self.get_left_height(node.left,l_height + 1)
        if node.right:
            self.get_left_height(node.right,l_height + 1)        
        return l_height 

    def get_right_height(self,node, r_height = 0) -> int:      
        """
        Gets the height of the right subtree of a current node.

        params node: The current node we are on
               l_height: to start, 0 is the value of the right subtree
               then we add one to the counter for each child.

        returns Int the height of the right subtree.
        """         
        if node.left:
            self.get_right_height(node.left,r_height + 1)
        if node.right:
            self.get_right_height(node.right,r_height + 1)        
        return r_height

    def _calculate_balance_factor(self):
        """
        Calculate the balance factor of the current node.

        Balance factor adds 1 to any parent with a left child,
        Balance factor subtracts 1 to any parent with a right child.
        Balance factor of a leaf is 0.

        """
        if self.left == None and self.right == None:
            self.balance_factor = 0

        if self.balance_factor > 1 or self.balance_factor < -1:
            self =  self.rotate()
            return self
        
        if self.parent == None:
            return self

        if self._is_left_child():
            self.parent.balance_factor += 1
            self.parent._calculate_balance_factor()

        elif self._is_right_child():
            self.parent.balance_factor -= 1
            self.parent._calculate_balance_factor()        
        return self

    def rotate(self):
        """
        After checking a nodes balance factor, if it is >= 2 or <= -2 perform
        a rotation.
        if left child, with left child only:
            perform LL rotation
            else: perform LR rotation
        if right child, with right child only:
            perform RR rotation
            else: perform RL rotation
        """
        if self.has_left_child_only():
            if self.left.has_left_child_only():
                #LL imbalance
                self.rotate_right()        
            else:
                #LR Imbalance
                old_root = self
                middle = self.left
                new_root = self.left.right
                old_root.parent = new_root
                old_root.parent.left = new_root
                old_root.left = None
                new_root.parent = None
                new_root.left = middle
                new_root.right = old_root
                middle.right = None
                old_root.balance_factor = (self.get_left_height(old_root) - self.get_right_height(old_root))
                self = new_root
                middle.balance_factor = (middle.get_left_height(middle) - middle.get_right_height(middle))
                self.balance_factor = (self.get_left_height(node=self) - self.get_right_height(node=self))
                return new_root
        else:
            if self.has_right_child_only():

                if self.right.has_right_child_only():
                    #RR imbalance
                    return self.rotate_left()                   
                else:
                    new_root = self.right.left
                    middle = self.right
                    old_root = self
                    new_root.parent = None
                    new_root.right = middle
                    new_root.left = old_root
                    middle.parent = new_root
                    middle.left = None
                    old_root.right = None
                    old_root.parent = new_root                   
                    old_root.balance_factor = (self.get_left_height(old_root) - self.get_right_height(old_root))
                    self = new_root
                    middle.balance_factor = (middle.get_left_height(middle) - middle.get_right_height(middle))
                    self.balance_factor = (self.get_left_height(node=self) - self.get_right_height(node=self))
                    return self   
        return self.find_root()

    def rotate_right(self):
        """
        Perform a RR rotaton.
        """
        old_root = self
        new_root = self.left
        new_root.left = old_root.left.left
        new_root.parent = old_root.parent
        old_root.parent = new_root
        if new_root.right:
            new_root.right.parent = old_root
            old_root.left = new_root.right
        else:
            old_root.left = None
        new_root.right = old_root
        if new_root.parent:
            new_root.parent.left = new_root
        self = new_root
        old_root.balance_factor = (self.get_left_height(old_root) - self.get_right_height(old_root))             
        self.balance_factor = (self.get_left_height(node=self) - self.get_right_height(node=self)) 
        self = self.find_root() 
        

    def rotate_left(self):
        """
        Perform a LL rotation.
        """
        old_root = self
        new_root = self.right
        new_root.parent = None
        new_root.left = old_root
        old_root.parent = new_root                   
        old_root.right = None                    
        self = new_root
        self.recalibrate_balance_factor_right(new_root, old_root)                 
        return self.find_root()

    def recalibrate_balance_factor_right(self, new_root, old_root):
        if old_root.left == None and old_root.right == None:
            old_root.balance_factor = 0
        else:
            old_root.balance_factor = (old_root.balance_factor + 1 - (min(new_root.balance_factor, 0)))
        new_root.balance_factor = (new_root.balance_factor + 1 + (max(old_root.balance_factor, 0)))
        
        return True

    def recalibrate_balance_factor_left(self, new_root, old_root):
        
        if old_root.left == None and old_root.right == None:
            old_root.balance_factor = 0
        else:
            old_root.balance_factor = (old_root.balance_factor - 1 - (max(new_root.balance_factor, 0)))
        new_root.balance_factor = (new_root.balance_factor - 1 + (min(old_root.balance_factor, 0)))
        return True

            
    
    def insert(self, node):
        if node.key <= self.key:
            if not self.has_left_child():
                self.left = node   
                node.parent=self
                #self._calculate_balance_factor(node)
                node._calculate_balance_factor() 
                return self.find_root()       
            else:
                self.left.insert(node)               
        else:
            if not self.has_right_child():
                self.right = node
                node.parent = self
                #self._calculate_balance_factor(node) 
                node._calculate_balance_factor()
                return self.find_root()             
            else:
                self.right.insert(node) 
        return self.find_root()
        
    
    def _is_left_child(self):
            return self.parent.left is self

    def _is_right_child(self):
            return self.parent.right is self

    def _is_root_node(self):
            return self.parent is None
 
    def is_leaf(self):
            return not (self.has_left_child() and self.has_right_child())

    def has_left_child(self):
        return not self.left is None

    def has_right_child(self):
        return not self.right is None

    def has_left_child_only(self):
        return not self.left is None and self.right is None

    def has_right_child_only(self):
        return not self.right is None and self.left is None

    def find_root(self):
        while self.parent:
            self = self.parent
        return self
   
    
