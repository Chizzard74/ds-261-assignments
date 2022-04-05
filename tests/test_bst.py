#BST Test Written by OSU DS-261

import unittest
import time
from data_structures.bst import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A BinarySearchTree exists.
        """
        try:
            BinarySearchTree()
        except NameError:
            self.fail("Could not instantiate BinarySearchTree.")

    def test_initial_attributes(self):
        """
        A BST is a recursive structure. When we refer to an object that "is a BST,"
        we are referring to a root node of a binary search tree.
        Every node has a left child, right child, and a key.
        A new BST has a left, right, key, and parent that are each None.
        Hint: Define an initializer.
        """
        bst = BinarySearchTree()
        self.assertIsNone(bst.left)
        self.assertIsNone(bst.right)
        self.assertIsNone(bst.key)
        self.assertIsNone(bst.parent)

    def test_instatiate_with_key(self):
        """
        A BST (node) can be instantiated with an initial key.
        When one isn't provided, the key is None.
        Hint: Use Python's 'default arguments' feature.
        """
        bst = BinarySearchTree()
        self.assertIsNone(bst.key)
        bst = BinarySearchTree(42)
        self.assertEqual(42, bst.key)

    """
    Cute, single-level trees. (Depth of zero.)
    """

    def test_insert_single_smaller(self):
        """
        Inserting a node into a single-level tree appends the new node as the
        left child, when the new node key is less than the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(1)
        bst.insert(child)
        self.assertEqual(child, bst.left)

    def test_parent_child_relationship(self):
        """
        Inserting a node into a single-level tree appends makes the new node
        a child of its parent node 
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(1)
        bst.insert(child)
        self.assertEqual(bst, child.parent)
        
    def test_insert_single_equal(self):
        """
        Inserting a node into a single-level tree appends the new node as the
        left child, when the new node value is equal to the the parent's key.
        (A new node whose key is <= parent key becomes the left child.)
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(5)
        bst.insert(child)
        self.assertEqual(child, bst.left)
        self.assertEqual(bst, child.parent)

    def test_insert_single_greater(self):
        """
        Inserting a node into a single-level tree appends the new node as the
        right child, when the new node key is greater than the parent's key.
        (A new node whose key is > parent key becomes the right child.)
        """
        bst = BinarySearchTree(5)
        child = BinarySearchTree(7)
        bst.insert(child)
        self.assertEqual(child, bst.right)
        self.assertEqual(bst, child.parent)

    def test_search_single_none(self):
        """
        Searching a single-level tree for a key that doesn't exist returns None.
        """
        bst = BinarySearchTree(5)
        self.assertIsNone(bst.search(-999))

    def test_search_single_one(self):
        """
        Searching a single-level tree for a key that does exist returns that node / tree.
        """
        bst = BinarySearchTree(5)
        self.assertEqual(bst, bst.search(5))

    def test_delete_single_nonexistent(self):
        """
        Deleting a node with a key that does not exist returns the root node of
        the single-level tree.
        """
        bst = BinarySearchTree(5)
        self.assertEqual(bst, bst.delete(-999))

    def test_delete_single(self):
        """
        Deleting the node of a single-level tree returns the node's parent.
        """
        bst = BinarySearchTree(5)
        self.assertIsNone(bst.delete(5))

    # """
    # Toddler, two-level trees. (Depth of one.)
    # # """

    def test_insert_two_smaller_left(self):
        """
        Inserting a node with a key that is less than the left child's key appends
        the new node as the left child's left child.
          5             5
         / \    =>     / \
        3   7         3   7
                     /
                    1
        Hint: Nest your logic. Delegate with recursion.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(1)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.left.left)
        self.assertEqual(left, child.parent)

    def test_insert_two_greater_left(self):
        """
        Inserting a node with a key that is greater than the left child's key
        (and less than the parent/root) appends the new node as the left child's
        right child.
          5             5
         / \    =>     / \
        3   7         3   7
                       \
                        4
        Hint: If this test immediately passes, you are on a happy path.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(4)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.left.right)
        self.assertEqual(left, child.parent)

    def test_insert_two_greater_right(self):
        """
        Inserting a node with a key that is greater than the right child's key
        appends the new node as the right child's right child.
          5             5
         / \    =>     / \
        3   7         3   7
                           \
                            9
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(9)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.right.right)
        self.assertEqual(right, child.parent)

    def test_insert_two_smaller_right(self):
        """
        Inserting a node with a key that is less than the right child's key
        (and greater than the parent/root) appends the new node as the right
        child's left child.
          5             5
         / \    =>     / \
        3   7         3   7
                         /
                        6
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        child = BinarySearchTree(6)
        bst.insert(left)
        bst.insert(right)
        bst.insert(child)
        self.assertEqual(child, bst.right.left)
        self.assertEqual(right, child.parent)

    def test_search_two_basics(self):
        """
        Searching a two-level tree for a key that doesn't exist returns None.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertIsNone(bst.search(-999))

    def test_search_two_root(self):
        """
        Searching a two-level tree for a key that exists in the root returns
        the root.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.search(5))

    def test_search_two_left(self):
        """
        Searching a two-level tree for a key that exists in the left subtree
        returns that left node / subtree.
        Hint: Try a brutish, 'naive' approach.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(left, bst.search(3))

    def test_search_two_right(self):
        """
        Searching a two-level tree for a key that exists in the right subtree
        returns that right node / subtree.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(right, bst.search(7))

    def test_delete_two_nonexistent(self):
        """
        Deleting a node with a key that does not exist does not modify the tree
        and returns the root node of the tree.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.delete(-999))
        self.assertEqual(5, bst.key)
        self.assertEqual(3, bst.left.key)
        self.assertEqual(7, bst.right.key)

    def test_delete_two_left_leaf(self):
        """
        Deleting the left child of a two-level tree removes the left child and
        returns the root node.
          5            5
         / \     =>     \
        3   7            7
        Hint: Consult the BST rules. Time to improve your `delete` method... a little.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.delete(3))
        self.assertIsNone(bst.left)
        self.assertEqual(5, bst.key)
        self.assertEqual(7, bst.right.key)

    def test_delete_two_right_leaf(self):
        """
        Deleting the right child of a two-level tree removes the right child and
        returns the root node.
          5            5
         / \     =>   /
        3   7        3
        Hint: Small changes to `delete`, lest you overthink it.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        right = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(right)
        self.assertEqual(bst, bst.delete(7))
        self.assertIsNone(bst.right)
        self.assertEqual(5, bst.key)
        self.assertEqual(3, bst.left.key)

    def test_delete_two_root_with_left(self):
        """
        Deleting the root of a two-level tree that has only a left child makes
        the left child the new root, and `delete` returns it.
          5
         /     =>  3
        3
        Hint: Small steps of a little nested logic.
        """
        bst = BinarySearchTree(5)
        initial_left_child = BinarySearchTree(3)
        bst.insert(initial_left_child)
        bst = bst.delete(5)
        self.assertEqual(initial_left_child, bst)
        self.assertEqual(3, bst.key)
        self.assertTrue(bst.is_leaf())
        self.assertIsNone(bst.parent)

    def test_delete_two_root_with_right(self):
        """
        Deleting the root of a two-level tree that has only a right child makes
        the right child the new root, and `delete` returns it.
        5
         \     =>  7
          7
        """
        bst = BinarySearchTree(5)
        initial_right_child = BinarySearchTree(7)
        bst.insert(initial_right_child)
        bst = bst.delete(5)
        self.assertEqual(initial_right_child, bst)
        self.assertEqual(7, bst.key)
        self.assertTrue(bst.is_leaf())
        self.assertIsNone(bst.parent)

    def test_delete_two_root(self):
        """
        Deleting the root of a two-level tree promotes the right child to be the
        new root, and `delete` returns it.
          5            7
         / \     =>   /
        3   7        3
        Hint: Consult the bst deletion rules... but be direct for now.
        """
        bst = BinarySearchTree(5)
        left = BinarySearchTree(3)
        initial_right_child = BinarySearchTree(7)
        bst.insert(left)
        bst.insert(initial_right_child)
        bst = bst.delete(5)
        self.assertEqual(initial_right_child, bst)
        self.assertEqual(3, bst.left.key)
        self.assertIsNone(bst.right)

    # """
    # Teen-age, three-level trees. (Depth of two.)
    # Hint: Don't just curse - be recursive.
    # """

    def test_insert_three_smaller_leftmost_leaf(self):
        """
        Inserting a node with a key that is less than the leftmost leaf node's
        key appends the new node as the leftmost leaf's left child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                         /
                        1
        Hint: Recursion, if you didn't already, makes this easy.
        """
        bst = BinarySearchTree(10)
        bst.insert(BinarySearchTree(5))
        bst.insert(BinarySearchTree(15))
        bst.insert(BinarySearchTree(2))
        bst.insert(BinarySearchTree(7))
        bst.insert(BinarySearchTree(12))
        bst.insert(BinarySearchTree(17))
        child = BinarySearchTree(1)
        bst.insert(child)
        self.assertEqual(child, bst.left.left.left)
        self.assertEqual(child.parent, bst.left.left)

    def test_insert_three_larger_leftmost_leaf(self):
        """
        Inserting a node with a key that is greater than the leftmost leaf node's
        key (but less than it's parents') appends the new node as the leftmost
        leaf's right child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                           \
                            3
        """
        bst = three_level_tree() # Same tree as pictured above to the left.
        child = BinarySearchTree(3)
        bst.insert(child)
        self.assertEqual(child, bst.left.left.right)
        self.assertEqual(child.parent, bst.left.left)

    def test_insert_three_smaller_left_right_leaf(self):
        """
        Inserting a node with a key that is less than the 'inner left' leaf node's
        key (but greater than it's parent and less than the root) appends the new
        node as the 'inner left' leaf's left child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                             /
                            6
        """
        bst = three_level_tree()
        child = BinarySearchTree(6)
        bst.insert(child)
        self.assertEqual(child, bst.left.right.left)
        self.assertEqual(child.parent, bst.left.right)

    def test_insert_three_larger_left_right_leaf(self):
        """
        Inserting a node with a key that is greater than the 'inner left' leaf node's
        key (but less than the root) appends the new node as the 'inner left' leaf's
        right child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                               \
                                8
        """
        bst = three_level_tree()
        child = BinarySearchTree(8)
        bst.insert(child)
        self.assertEqual(child, bst.left.right.right)
        self.assertEqual(child.parent, bst.left.right)

    def test_insert_three_smaller_right_left_leaf(self):
        """
        Inserting a node with a key that is less than the 'inner right' leaf node's
        key (and less than it's parent, but greater than the root) appends the
        new node as the 'inner right' leaf's left child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                                /
                               11
        """
        bst = three_level_tree()
        child = BinarySearchTree(11)
        bst.insert(child)
        self.assertEqual(child, bst.right.left.left)
        self.assertEqual(child.parent, bst.right.left)

    def test_insert_three_larger_right_left_leaf(self):
        """
        Inserting a node with a key that is greater than the 'inner right' leaf
        node's key (but less than it's parent) appends the new node as the
        'inner right' leaf's right child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                                   \
                                   13
        """
        bst = three_level_tree()
        child = BinarySearchTree(13)
        bst.insert(child)
        self.assertEqual(child, bst.right.left.right)
        self.assertEqual(child.parent, bst.right.left)

    def test_insert_three_smaller_right_right_leaf(self):
        """
        Inserting a node with a key that is less than the rightmost leaf node's
        key (but greater than it's parent) appends the new node as the rightmost
        leaf's left child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                                     /
                                   16
        """
        bst = three_level_tree()
        child = BinarySearchTree(16)
        bst.insert(child)
        self.assertEqual(child, bst.right.right.left)
        self.assertEqual(child.parent, bst.right.right)

    def test_insert_three_greater_right_right_leaf(self):
        """
        Inserting a node with a key that is less than the rightmost leaf node's
        key (but greater than it's parent) appends the new node as the rightmost
        leaf's left child.
             10                10
           /    \            /    \
          5      15    =>   5      15
         / \    /  \       / \    /  \
        2   7  12   17    2   7  12   17
                                       \
                                        19
        """
        bst = three_level_tree()
        child = BinarySearchTree(19)
        bst.insert(child)
        self.assertEqual(child, bst.right.right.right)
        self.assertEqual(child.parent, bst.right.right)

    def test_search_three_not_found(self):
        """
        Searching for a non-existent key in a three-level tree returns None.
        """
        bst = three_level_tree()
        self.assertIsNone(bst.search(-999))

    def test_search_three_root(self):
        """
        Searching a three-level tree for a key that exists in the root returns
        the root.
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.search(10))

    def test_search_three_outer_left(self):
        """
        Searching a three-level tree for a key that exists in the leftmost leaf
        returns that leftmost leaf.
        Hint: Be recursive.
        """
        bst = three_level_tree()
        self.assertEqual(bst.left.left, bst.search(2))

    def test_search_three_inner_left(self):
        """
        Searching a three-level tree for a key that exists in the inner left leaf
        returns that inner left leaf.
        """
        bst = three_level_tree()
        self.assertEqual(bst.left.right, bst.search(7))

    def test_search_three_inner_right(self):
        """
        Searching a three-level tree for a key that exists in the inner right leaf
        returns that inner right leaf.
        """
        bst = three_level_tree()
        self.assertEqual(bst.right.left, bst.search(12))

    def test_search_three_outer_right(self):
        """
        Searching a three-level tree for a key that exists in the rightmost leaf
        returns that rightmost leaf.
        """
        bst = three_level_tree()
        self.assertEqual(bst.right.right, bst.search(17))

    # """
    # Before proper deletions, let's add some convenience methods.
    # """

    def test_is_leaf(self):
        """
        A node without children is a leaf node.
        """
        bst = BinarySearchTree(10)
        self.assertTrue(bst.is_leaf())

    def test_with_left_child_is_not_leaf(self):
        """
        A node with a left child is not a leaf node.
        """
        bst = BinarySearchTree(10)
        bst.left = BinarySearchTree(5)
        self.assertFalse(bst.is_leaf())

    def test_with_right_child_is_not_leaf(self):
        """
        A node with a right child is not a leaf node.
        """
        bst = BinarySearchTree(10)
        bst.right = BinarySearchTree(15)
        self.assertFalse(bst.is_leaf())

    def test_has_left_child(self):
        """
        A node with a left child returns True.
        """
        bst = BinarySearchTree(10)
        bst.insert(BinarySearchTree(5))
        self.assertTrue(bst.has_left_child())

    def test_not_has_left_child(self):
        """
        A node without a left child returns False.
        """
        bst = BinarySearchTree(10)
        self.assertFalse(bst.has_left_child())

    def test_has_right_child(self):
        """
        A node with a right child returns True.
        """
        bst = BinarySearchTree(10)
        bst.left = BinarySearchTree(15)
        self.assertTrue(bst.has_left_child())

    def test_not_has_right_child(self):
        """
        A node without a right child returns False.
        """
        bst = BinarySearchTree(10)
        self.assertFalse(bst.has_right_child())

    def test_find_minimum_one(self):
        """
        A tree's 'minimum' node is the one with the smallest key.
        """
        bst = BinarySearchTree(10)
        self.assertEqual(bst, bst.minimum())

    def test_find_minimum_two(self):
        """
        A tree's 'minimum' node is the one with the smallest key.
        """
        bst = BinarySearchTree(10)
        left = BinarySearchTree(5)
        right = BinarySearchTree(15)
        bst.left = left
        bst.right = right
        self.assertEqual(left, bst.minimum())

    def test_find_minimum_three(self):
        """
        A tree's 'minimum' node is the one with the smallest key.
        Hint: The recipe is simple. And recursive.
        """
        bst = three_level_tree()
        self.assertEqual(bst.left.left, bst.minimum())

    # # If all of your tests are passing, try refactoring your implementation by
    # # using those new convenience methods. One change at a time, keeping the
    # # tests passing.

    def test_delete_three_nonexistent(self):
        """
        Deleting a node with a key that does not exist does not modify the tree
        and returns the root node of a three-level tree.
             10                   10
           /    \               /    \
          5      15      =>    5      15
         / \    /  \          / \    /  \
        2   7  12   17       2   7  12   17
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.delete(-999))
        self.assertEqual(10, bst.key)
        self.assertEqual(5, bst.left.key)
        self.assertEqual(15, bst.right.key)
        self.assertEqual(2, bst.left.left.key)
        self.assertEqual(7, bst.left.right.key)
        self.assertEqual(12, bst.right.left.key)
        self.assertEqual(17, bst.right.right.key)

    def test_delete_three_leftmost_leaf(self):
        """
        Deleting the leftmost leaf of a three-level tree removes the leftmost leaf
        and returns the root node of the three-level tree.
             10                   10
           /    \               /    \
          5      15      =>    5      15
         / \    /  \            \    /  \
        2   7  12   17           7  12   17
        Hint: Consult the BST rules. Use paper. Draw pictures, hand-write code.
              Be recursive.
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.delete(2))
        self.assertIsNone(bst.left.left)
        self.assertEqual(10, bst.key)
        self.assertEqual(5, bst.left.key)
        self.assertEqual(15, bst.right.key)
        self.assertEqual(7, bst.left.right.key)
        self.assertEqual(12, bst.right.left.key)
        self.assertEqual(17, bst.right.right.key)

    def test_delete_three_inner_left_leaf(self):
        """
        Deleting the 'inner left' leaf of a three-level tree removes the inner
        left leaf and returns the root node of the three-level tree.
             10                   10
           /    \               /    \
          5      15      =>    5      15
         / \    /  \          /      /  \
        2   7  12   17       2      12   17
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.delete(7))
        self.assertIsNone(bst.left.right)
        self.assertEqual(10, bst.key)
        self.assertEqual(5, bst.left.key)
        self.assertEqual(15, bst.right.key)
        self.assertEqual(2, bst.left.left.key)
        self.assertEqual(12, bst.right.left.key)
        self.assertEqual(17, bst.right.right.key)

    def test_delete_three_inner_right_leaf(self):
        """
        Deleting the 'inner right' leaf of a three-level tree removes the inner
        right leaf and returns the root node of the three-level tree.
             10                   10
           /    \               /    \
          5      15      =>    5      15
         / \    /  \          / \       \
        2   7  12   17       2   7       17
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.delete(12))
        self.assertIsNone(bst.right.left)
        self.assertEqual(10, bst.key)
        self.assertEqual(5, bst.left.key)
        self.assertEqual(15, bst.right.key)
        self.assertEqual(2, bst.left.left.key)
        self.assertEqual(7, bst.left.right.key)
        self.assertEqual(17, bst.right.right.key)

    def test_delete_three_rightmost_leaf(self):
        """
        Deleting the rightmost leaf of a three-level tree removes the rightmost
        leaf and returns the root node of the three-level tree.
             10                   10
           /    \               /    \
          5      15      =>    5      15
         / \    /  \          / \    /
        2   7  12   17       2   7  12
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.delete(17))
        self.assertIsNone(bst.right.right)
        self.assertEqual(10, bst.key)
        self.assertEqual(5, bst.left.key)
        self.assertEqual(15, bst.right.key)
        self.assertEqual(2, bst.left.left.key)
        self.assertEqual(7, bst.left.right.key)
        self.assertEqual(12, bst.right.left.key)

    def test_delete_three_left(self):
        """
        Deleting a node with two children causes the leaf with the smallest key
        in the deleted node's right subtree to take its place; and, delete still
        returns the root of the tree.
             10                   10
           /    \               /    \
          5      15      =>    7      15
         / \    /  \          /      /  \
        2   7  12   17       2      12   17
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.delete(5))
        self.assertEqual(7, bst.left.key)
        self.assertIsNone(bst.left.right)
        self.assertEqual(10, bst.key)
        self.assertEqual(15, bst.right.key)
        self.assertEqual(2, bst.left.left.key)
        self.assertEqual(12, bst.right.left.key)
        self.assertEqual(17, bst.right.right.key)

    def test_delete_three_right(self):
        """
        Deleting a node with two children causes the leaf with the smallest key
        in the deleted node's right subtree to take its place; and, delete still
        returns the root of the tree.
             10                   10
           /    \               /    \
          5      15      =>    5      17
         / \    /  \          / \    /
        2   7  12   17       2   7  12
        """
        bst = three_level_tree()
        self.assertEqual(bst, bst.delete(15))
        self.assertEqual(17, bst.right.key)
        self.assertIsNone(bst.right.right)
        self.assertEqual(10, bst.key)
        self.assertEqual(5, bst.left.key)
        self.assertEqual(2, bst.left.left.key)
        self.assertEqual(7, bst.left.right.key)
        self.assertEqual(12, bst.right.left.key)

    def test_delete_three_root(self):
        """
        Deleting a node with two children causes the leaf with the smallest key
        in the deleted node's right subtree to take its place; and, delete still
        returns the root of the tree.
             10                   12
           /    \               /    \
          5      15      =>    5      15
         / \    /  \          / \       \
        2   7  12   17       2   7       17
        """
        bst = three_level_tree()
        bst = bst.delete(10)
        self.assertEqual(12, bst.key)
        self.assertEqual(5, bst.left.key)
        self.assertEqual(15, bst.right.key)
        self.assertEqual(2, bst.left.left.key)
        self.assertEqual(7, bst.left.right.key)
        self.assertIsNone(bst.right.left)
        self.assertEqual(17, bst.right.right.key)

    # """
    # Mature, N-level trees.
    # """

    def test_insertions(self):
        """
             10                   10                      10
           /    \               /    \                  /    \
          5      15      =>    5      15         =>    5      15
         / \    /  \          / \    /  \             / \    /  \
        2   7  12   17       2   7  12   17          2   7  12   30
                                        /  \                    /  \
                                       16  45                 16   45
                                          /  \                       \
                                         30   99                     99
        """
        bst = three_level_tree()
        bst.insert(BinarySearchTree(45))
        bst.insert(BinarySearchTree(16))
        bst.insert(BinarySearchTree(30))
        bst.insert(BinarySearchTree(99))
        self.assertEqual(45, bst.right.right.right.key)
        self.assertEqual(99, bst.right.right.right.right.key)
        bst.delete(17)
        bst.delete(5)
        self.assertEqual(7, bst.left.key)
        self.assertEqual(30, bst.right.right.key)
        self.assertEqual(16, bst.right.right.left.key)
        self.assertEqual(45, bst.right.right.right.key)
        self.assertEqual(99, bst.right.right.right.right.key)
        self.assertIsNone(bst.right.right.right.left)

    # """
    # Traversals
    # """

    def test_one_pre_order(self):
        """
        The pre-order traversal of a single-node tree is a list containing that
        node's key.
        """
        bst = BinarySearchTree(10)
        self.assertEqual([10], bst.keys('pre'))

    def test_one_in_order(self):
        """
        The in-order traversal of a single-node tree is a list containing that
        node's key.
        """
        bst = BinarySearchTree(5)
        self.assertEqual([5], bst.keys('in'))

    def test_one_post_order(self):
        """
        The post-order traversal of a single-node tree is a list containing that
        node's key.
        """
        bst = BinarySearchTree(3)
        self.assertEqual([3], bst.keys('post'))

    def test_two_pre_order(self):
        """
        The pre-order traversal of a two-level tree is a list containing the keys
        in 'pre-order'.
          5
         / \    => [5, 3, 7]
        3   7
        """
        bst = BinarySearchTree(5)
        bst.left = BinarySearchTree(3)
        bst.right = BinarySearchTree(7)
        self.assertEqual([5, 3, 7], bst.keys('pre'))

    def test_two_in_order(self):
        """
        The in-order traversal of a two-level tree is a list containing the keys
        in 'in-order'.
          5
         / \    => [3, 5, 7]
        3   7
        """
        bst = BinarySearchTree(5)
        bst.left = BinarySearchTree(3)
        bst.right = BinarySearchTree(7)
        self.assertEqual([3, 5, 7], bst.keys('in'))

    def test_two_post_order(self):
        """
        The post-order traversal of a two-level tree is a list containing the keys
        in 'post-order'.
          5
         / \    => [3, 7, 5]
        3   7
        """
        bst = BinarySearchTree(5)
        bst.left = BinarySearchTree(3)
        bst.right = BinarySearchTree(7)
        self.assertEqual([3, 7, 5], bst.keys('post'))

    def test_three_pre_order(self):
        """
        The pre-order traversal of a three-level tree is a list containing the keys
        in 'pre-order'.
             10
           /    \
          5      15      => [10, 5, 2, 7, 15, 12, 17]
         / \    /  \
        2   7  12   17
        """
        bst = three_level_tree()
        self.assertEqual([10, 5, 2, 7, 15, 12, 17], bst.keys('pre'))

    def test_three_in_order(self):
        """
        The in-order traversal of a three-level tree is a list containing the keys
        in 'in-order'.
             10
           /    \
          5      15      => [2, 5, 7, 10, 12, 15, 17]
         / \    /  \
        2   7  12   17
        """
        bst = three_level_tree()
        self.assertEqual([2, 5, 7, 10, 12, 15, 17], bst.keys('in'))

    def test_three_post_order(self):
        """
        The post-order traversal of a three-level tree is a list containing the keys
        in 'post-order'.
             10
           /    \
          5      15      => [2, 7, 5, 12, 17, 15, 10]
         / \    /  \
        2   7  12   17
        """
        bst = three_level_tree()
        self.assertEqual([2, 7, 5, 12, 17, 15, 10], bst.keys('post'))


def three_level_tree():
    """
         10
       /    \
      5      15
     / \    /  \
    2   7  12   17
    """
    bst = BinarySearchTree(10)
    bst.insert(BinarySearchTree(5))
    bst.insert(BinarySearchTree(15))
    bst.insert(BinarySearchTree(2))
    bst.insert(BinarySearchTree(7))
    bst.insert(BinarySearchTree(12))
    bst.insert(BinarySearchTree(17))
    return bst


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
