#Test created by OSU 261 DS
#Test the AVLTree

import unittest
import time
from data_structures.avl import AVLTree


class TestBinarySearchTree(unittest.TestCase):

    # """
    # Initialization
    # """

    def test_instantiation(self):
        """
        A AVLTree exists.
        """
        try:
            AVLTree()
        except NameError:
            self.fail("Could not instantiate AVLTree.")

    def test_initial_attributes(self):
        """
        A AVL tree is a recursive structure. When we refer to an object,
        we are referring to a node of the AVL tree.
        Every node has a left child, right child, key, parent, and balance_factor.
        A new AVL tree has a left, right, key, and parent that are each None, and a
        balance_factor equal to 0.
        Hint: Define an initializer.
        """
        avl = AVLTree()
        self.assertIsNone(avl.left)
        self.assertIsNone(avl.right)
        self.assertIsNone(avl.key)
        self.assertIsNone(avl.parent)
        self.assertEqual(0,avl.balance_factor)
  
    # """
    # # Calculating the balance factor of each node 
    # #        10
    # #           \
    # #            20 
    # # """
    
    def test_balance_factor_depth1_right(self):
        """
        The balance_factor of a node is the height of its left subtree
        minus the height of its right subtree.
        Hint: create helper method _caculateBalanceFactor and call it from insert after inserting a node
        Hint2: work from the node you're inserting up to the root recursively,
        modifying your parent's balance factor as you go
        """
        avl = AVLTree(10)
        avl.insert(AVLTree(20))
        
        self.assertEqual(-1,avl.balance_factor)
        self.assertEqual(0,avl.right.balance_factor)
        
    # # """
    # # Calculating the balance factor of each node 
    # #            10
    # #           /
    # #          5 
    # # """
    
    def test_balance_factor_depth1_left(self):
        """
        The balance_factor of a node is the height of its left subtree
        minus the height of its right subtree.
        Hint: create helper method _caculateBalanceFactor and call it from insert after inserting a node
        Hint2: work from the node you're inserting up to the root recursively,
        modifying your parent's balance factor as you go
        """
        avl = AVLTree(10)
        avl.insert(AVLTree(5))
        self.assertEqual(1,avl.balance_factor)
        self.assertEqual(0,avl.left.balance_factor)
        
        
    # # # """
    # # # Calculating the balance factor of each node 
    # # #        10
    # # #       /   \
    # # #      5     20 
    # # #              \
    # # #               30
    # # # """
    
    def test_balance_factor_depth2_right(self):
        """
        The balance_factor of a node is the height of its left subtree
        minus the height of its right subtree.
        Hint: create helper method _caculateBalanceFactor and call it from insert after inserting a node
        Hint2: work from the node you're inserting up to the root recursively,
        modifying your parent's balance factor as you go
        """
        avl = AVLTree(10)
        avl.insert(AVLTree(5))
        avl.insert(AVLTree(20))
        avl.insert(AVLTree(30))
        self.assertEqual(-1,avl.balance_factor)
        self.assertEqual(-1,avl.right.balance_factor)
        self.assertEqual(0,avl.right.right.balance_factor)
        self.assertEqual(0,avl.left.balance_factor)


    # # # # """
    # # # # Calculating the balance factor of each node 
    # # # #            10
    # # # #           /  \
    # # # #          5    20
    # # # #         /
    # # # #        1
    # # # # """
    
    def test_balance_factor_depth2_left(self):
        """
        The balance_factor of a node is the height of its left subtree
        minus the height of its right subtree.
        Hint: create helper method _calculateBalanceFactor and call it from insert after inserting a node
        Hint2: work from the node you're inserting up to the root recursively,
        modifying your parent's balance factor as you go
        """
        avl = AVLTree(10)
        avl.insert(AVLTree(5))
        avl.insert(AVLTree(20))
        avl.insert(AVLTree(1))
        self.assertEqual(1,avl.balance_factor)
        self.assertEqual(1,avl.left.balance_factor)
        self.assertEqual(0,avl.left.left.balance_factor)
        self.assertEqual(0,avl.right.balance_factor)
    
    # # # """
    # # # # RR Imbalance, left rotation
    # # # # When node 30 ia inserted, detect a RR imbalance and rotate
    # # # # left around node 10
    # # # #        10                     20
    # # # #           \                  /  \
    # # # #            20     =>        10   30
    # # # #              \
    # # # #               30
    # # # # """
    
    def test_left_rotation(self):
        """
        Inserting node 30 causes a RR imbalance. 
        Rotates left around node 10 returning the new root (node 20)
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(20))
        avl = avl.insert(AVLTree(30))
        self.assertEqual(20,avl.key)
        self.assertEqual(30,avl.right.key)
        self.assertEqual(10,avl.left.key)
    
        
    # # # # """
    # # # # recalculate the balance factor for the old root (10) and the new root (20). Note: All other
    # # # # balance factors stay the same and do not need to be recalculated.
    # # # # Formulas to recalculate balance factors after a left rotation are provided in your reading and 
    # # # # given here for your convenience.
    # # # #
    # # # #  old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
    # # # #  new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)
    # # # #
    # # # # In this example 10 is old root and 20 is new root
    # # # # 
    # # # #        10                     20
    # # # #           \                  /  \
    # # # #            20     =>        10   30
    # # # #              \
    # # # #               30
    # # # # """
    
    def test_recalculate_balance_factors_after_left_rotation(self):
        """
        Inserting node 30 causes a RR imbalance. 
        Rotate left and recalculate the load factors for the old root and the new root
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(20))
        avl = avl.insert(AVLTree(30))
        self.assertEqual(0,avl.balance_factor)
        self.assertEqual(0,avl.right.balance_factor)
        self.assertEqual(0,avl.left.balance_factor)
        
    # # # """
    # # # # LL Imbalance, right rotation
    # # # # When node 1 ia inserted, detect a LL imbalance and rotate
    # # # # right around node 10
    # # # #        10                  5
    # # # #        /                  /  \
    # # # #       5     =>           1   10
    # # # #      /
    # # # #     1
    # # # # """
    
    def test_right_rotation(self):
        """
        Inserting node 1 causes a LL imbalance. 
        Rotates right around node 10 returning the new root (node 5)
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(5))
        avl = avl.insert(AVLTree(1))
        self.assertEqual(5,avl.key)
        self.assertEqual(10,avl.right.key)
        self.assertEqual(1,avl.left.key)
       
    # # # # """
    # # # # recalculate the balance factor for the old root (10) and the new root (5). Note: All other
    # # # # balance factors stay the same and do not need to be recalculated.
    # # # # Formulas to recalculate balance factors after a right rotation are provided in your reading and 
    # # # # given here for your convenience.
    # # # #
    # # # #  old_root.balance_factor = old_root.balance_factor - 1 - mmax(new_root.balance_factor, 0)
    # # # #  new_root.balance_factor = new_root.balance_factor - 1 + mim(old_root.balance_factor, 0)
    # # # #
    # # # # In this example 10 is old root and 5 is new root
    # # # # 
    # # # #        10                  5
    # # # #        /                  /  \
    # # # #       5     =>           1   10
    # # # #      /
    # # # #     1
    # # # """
    
    def test_recalculate_balance_factors_after_right_rotation(self):
        """
        Inserting node 1 causes a LL imbalance. 
        Rotate right and recalculate the load factors for the old root and the new root
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(5))
        avl = avl.insert(AVLTree(1))
        self.assertEqual(0,avl.balance_factor)
        self.assertEqual(0,avl.right.balance_factor)
        self.assertEqual(0,avl.left.balance_factor)
        
    # # # # """
    # # # # When node 15 ia inserted, detect a RL imbalance. To rebalance, its a 2 step process
    # # # # First, perform a right rotation around node 20.
    # # # # Then, perform a left rotation around node 10
    # # # # 
    # # # #        10            10            15
    # # # #           \            \           / \
    # # # #            20     =>    15  =>    10  20
    # # # #            /             \
    # # # #          15               20
    # # # #
    # # # # HINT:  In this case, the balance factor of node 10 is -2 (its the nearest unbalanced ancestor) 
    # # # # and the balance factor of node 20 (its right child) is 1. If this were not the 
    # # # # case, it would be a RR imbalance, requiring a single left rotation  
    # # # # 
    # # # # """
    
    def test_right_left_rotation(self):
        """
        Inserting node 15 causes a RL imbalance. 
        Results in a rotate right around node 20 followed by a rotate left around node 10
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(20))
        avl = avl.insert(AVLTree(15))
        self.assertEqual(15,avl.key)
        self.assertEqual(20,avl.right.key)
        self.assertEqual(10,avl.left.key)
    
        
    # # # # """
    # # # # recalculate the balance factor for the old root  and the new root. Note: All other
    # # # # balance factors stay the same and do not need to be recalculated.
    # # # # Formulas to recalculate balance factors after rotations are provided in your reading and 
    # # # # given here for your convenience.
    # # # #
    # # # #  Balance factor formulas after a left rotation:
    # # # #  old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
    # # # #  new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)
    # # # #
    # # # #  Balance factor formulas after a right rotation:
    # # # #  old_root.balance_factor = old_root.balance_factor - 1 - mmax(new_root.balance_factor, 0)
    # # # #  new_root.balance_factor = new_root.balance_factor - 1 + mim(old_root.balance_factor, 0)
    # # # #
    # # # # In this example, for the first rotation, 20 is old root and 15 is new root (right rotation around node 20)
    # # # # For the second rotation, 10 is the old root and 16 is the new root (left rotation around node 10)
    # # # # 
    # # # #        10            10            15
    # # # #           \            \           / \
    # # # #            20     =>    15  =>    10  20
    # # # #            /             \
    # # # #          15               20
    # # # # """
    
    def test_recalculate_balance_factors_after_right_left_rotation(self):
        """
        Inserting node 15 causes a RL imbalance. 
        Results in a rotate right around node 20 followed by a rotate left around node 10
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(20))
        avl = avl.insert(AVLTree(15))
        self.assertEqual(0,avl.balance_factor)
        self.assertEqual(0,avl.right.balance_factor)
        self.assertEqual(0,avl.left.balance_factor)
        
    # # # # """
    # # # # When node 7 ia inserted, detect a LR imbalance. To rebalance, its a 2 step process
    # # # # First, perform a left rotation around node 5.
    # # # # Then, perform a right rotation around node 10
    # # # # 
    # # # #        10           10        7
    # # # #        /            /        /  \
    # # # #       5     =>     7        5   10
    # # # #        \          /
    # # # #         7        5
    # # # #
    # # # # HINT:  In this case, the balance factor of node 10 is 22 (its the nearest unbalanced ancestor) 
    # # # # and the balance factor of node 5 (its left child) is -1. If this were not the 
    # # # # case, it would be a LL imbalance, requiring a single right rotation  
    # # # # 
    # # # # """
    
    def test_left_right_rotation(self):
        """
        Inserting node 7 causes a LR imbalance. 
        Results in a rotate left around node 5 followed by a rotate right around node 10
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(5))
        avl = avl.insert(AVLTree(7))
        self.assertEqual(7,avl.key)
        self.assertEqual(10,avl.right.key)
        self.assertEqual(5,avl.left.key)
    
        
    # # # # """
    # # # # recalculate the balance factor for the old root  and the new root. Note: All other
    # # # # balance factors stay the same and do not need to be recalculated.
    # # # # Formulas to recalculate balance factors after rotations are provided in your reading and 
    # # # # given here for your convenience.
    # # # #
    # # # #  Balance factor formulas after a left rotation:
    # # # #  old_root.balance_factor = old_root.balance_factor + 1 - min(new_root.balance_factor, 0)
    # # # #  new_root.balance_factor = new_root.balance_factor + 1 + max(old_root.balance_factor, 0)
    # # # #
    # # # #  Balance factor formulas after a right rotation:
    # # # #  old_root.balance_factor = old_root.balance_factor - 1 - mmax(new_root.balance_factor, 0)
    # # # #  new_root.balance_factor = new_root.balance_factor - 1 + mim(old_root.balance_factor, 0)
    # # # #
    
    # # # # In this example, for the first rotation, 5 is old root and 7 is new root (left rotation around node 5)
    # # # # For the second rotation, 10 is the old root and 7 is the new root (right rotation around node 10)
    # # # # 
    # # # #        10           10        7
    # # # #        /            /        /  \
    # # # #       5     =>     7        5   10
    # # # #        \          /
    # # # #         7        5
    # # # # """
    
    def test_recalculate_balance_factors_after_left_right_rotation(self):
        """
        Inserting node 7 causes a LR imbalance. 
        Results in a rotate left around node 5 followed by a rotate right around node 10
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(5))
        avl = avl.insert(AVLTree(7))
        self.assertEqual(0,avl.balance_factor)
        self.assertEqual(0,avl.right.balance_factor)
        self.assertEqual(0,avl.left.balance_factor)
        
    def test_larger_tree_LL_imbalance(self):
        """
        Inserting node 1 causes a LL imbalance. 
        Results in a rotate right around node 5 
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(5))
        avl = avl.insert(AVLTree(20))
        avl = avl.insert(AVLTree(3))
        avl = avl.insert(AVLTree(1))
        self.assertEqual(10,avl.key)
        self.assertEqual(20,avl.right.key)
        self.assertEqual(3,avl.left.key)
        self.assertEqual(1,avl.left.left.key)
        self.assertEqual(5,avl.left.right.key)
        #self.assertEqual(5,avl.left.right.key)
        # self.assertEqual(0,avl.balance_factor)
        # self.assertEqual(0,avl.right.balance_factor)
        # self.assertEqual(0,avl.left.balance_factor)
            
    def test_larger_tree_LL_balance_factors(self):
        """
        Inserting node 1 causes a LL imbalance. 
        Results in a rotate right around node 5 
        """
        avl = AVLTree(10)
        avl = avl.insert(AVLTree(5))
        avl = avl.insert(AVLTree(20))
        avl = avl.insert(AVLTree(3))
        avl = avl.insert(AVLTree(1))
        self.assertEqual(1,avl.balance_factor)
        self.assertEqual(0,avl.right.balance_factor)
        self.assertEqual(0,avl.left.balance_factor)
        self.assertEqual(0,avl.left.left.balance_factor)
        self.assertEqual(0,avl.left.right.balance_factor)

if __name__ == '__main__':
    unittest.main()
