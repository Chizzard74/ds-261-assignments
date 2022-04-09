#Test created by OSU 261 DS


import unittest
import time
from data_structures.stack import Stack


class TestStack(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Stack exists.
        """
        try:
            Stack()
        except NameError:
            self.fail("Could not instantiate Stack.")

    def test_initially_empty(self):
        """
         A stack is initially empty.
        """
        s = Stack()
        self.assertTrue(s.is_empty())

    def test_initial_pop(self):
        """
        Popping from an empty stack raises IndexError.
        """
        s = Stack()
        self.assertRaises(IndexError, s.pop)

    def test_initial_peek(self):
        """
        Peeking at an empty stack raises IndexError.
        """
        s = Stack()
        self.assertRaises(IndexError, s.peek)

    def test_initial_push(self):
        """
        Pushing a value onto the stack means the stack is no longer empty.
        """
        s = Stack()
        s.push('fee')
        self.assertFalse(s.is_empty())

    def test_peek_one(self):
        """
        A value pushed onto the stack can be peeked at.
        """
        s = Stack()
        s.push('fee')
        self.assertEqual('fee', s.peek())

    def test_pop_one(self):
        """
        A value pushed onto the stack can be popped.
        """
        s = Stack()
        s.push('fee')
        self.assertEqual('fee', s.pop())

    def test_peek_two(self):
        """
        Peeking at a stack with two values returns the last pushed value.
        """
        s = Stack()
        s.push('fee')
        s.push('fi')
        self.assertEqual('fi', s.peek())

    def test_peek_state(self):
        """
        Peeking doesn't mutate the stack.
        """
        s = Stack()
        s.push('fee')
        s.push('fi')
        self.assertEqual('fi', s.peek())
        self.assertEqual('fi', s.peek())

    def test_pop_two(self):
        """
        Popping from a stack with two values returns the last pushed value.
        """
        s = Stack()
        first_value = fake_value()
        second_value = fake_value()
        s.push(first_value)
        s.push(second_value)
        self.assertEqual(second_value, s.pop())

    def test_pop_state(self):
        """
        Popping removes the last pushed value from the stack.
        """
        s = Stack()
        first_value = fake_value()
        second_value = fake_value()
        s.push(first_value)
        s.push(second_value)
        self.assertEqual(second_value, s.pop())
        self.assertEqual(first_value, s.pop())
        self.assertTrue(s.is_empty())


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
