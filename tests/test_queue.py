#Test created by OSU 261 DS

import unittest
import time
from data_structures.queue import Queue

# Hint: Once test_has_linked_list_internal passes, uncomment this line.
# Refer to https://ajakubek.github.io/python-llist/index.html for sllist documentation
from llist import sllist


class TestQueue(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Queue exists.
        """
        try:
            Queue()
        except NameError:
            self.fail("Could not instantiate Queue.")

    def test_initial_size(self):
        """
        A queue size is initially zero
        """
        q = Queue()
        self.assertEqual(0,q.items)

    # """
    # Guiding enqueuing and dequeuing with internal storage
    # """

    def test_has_linked_list_internal(self):
        """
        A queue has a data member, which is an sllist.
        """
        from llist import sllist # Hint: pip3 install llist
        q = Queue()
        self.assertEqual(sllist, type(q.data))

    # # Hint: Once test_has_linked_list_internal passes, uncomment the import at
    # #       the top of this file.

    def test_enqueue_one_internal(self):
        """
        Enqueueing a value adds it to the internal sllist.
        """
        q = Queue()
        q.enqueue('fee')
        self.assertEqual('fee', q.data.first.value)

    def test_enqueue_two_internal(self):
        """
        Enqueueing two values results in the first enqueued value being the first
        one in the list, and the second value being the last one in the list.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        self.assertEqual('fee', q.data.first.value)
        self.assertEqual('fi', q.data.last.value)

    def test_enqueue_three_internal(self):
        """
        Enqueueing three values results in the first enqueued value being the first
        one in the list, and the third value being the last one in the list.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        q.enqueue('fo')
        self.assertEqual('fee', q.data.first.value)
        self.assertEqual('fo', q.data.last.value)

    def test_dequeue_one(self):
        """
        Dequeuing from a single-element queue returns the single value.
        """
        q = Queue()
        q.enqueue('fee')
        self.assertEqual('fee', q.dequeue())

    def test_dequeue_one_internal(self):
        """
        Dequeuing from a single-element queue removes it from the internal sllist.
        """
        q = Queue()
        q.enqueue('fee')
        self.assertEqual(1, q.data.size)
        _ = q.dequeue()
        self.assertEqual(0, q.data.size)

    def test_dequeue_two(self):
        """
        Dequeuing from a two-element queue returns the first enqueued value.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        self.assertEqual('fee', q.dequeue())

    def test_dequeue_two_internal(self):
        """
        Dequeuing from a two-element queue removes the first enqueued value from
        the sllist.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        _ = q.dequeue()
        self.assertEqual('fi', q.data.first.value)

    def test_dequeue_three(self):
        """
        Dequeuing from a three-element queue returns each enqueued value in FIFO
        order.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        q.enqueue('fo')
        self.assertEqual('fee', q.dequeue())
        self.assertEqual('fi', q.dequeue())
        self.assertEqual('fo', q.dequeue())

    def test_dequeue_three_internal(self):
        """
        Dequeuing from a three-element queue removes each dequeued value from
        the internal sllist, in FIFO order.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        q.enqueue('fo')
        _ = q.dequeue()
        self.assertEqual('fi', q.data.first.value)
        _ = q.dequeue()
        self.assertEqual('fo', q.data.first.value)


    # """
    # Emptiness
    # """

    def test_empty(self):
        """
        A queue is initially empty.
        """
        q = Queue()
        self.assertTrue(q.is_empty())

    def test_not_empty(self):
        """
        A queue with one enqueued value is not empty.
        """
        q = Queue()
        q.enqueue('fee')
        self.assertFalse(q.is_empty())

    def test_empty_after_dequeue(self):
        """
        A queue with one enqueued value is empty after dequeuing.
        """
        q = Queue()
        q.enqueue('fee')
        _ = q.dequeue()
        self.assertTrue(q.is_empty())

    def test_not_empty_multiple(self):
        """
        A queue with two enqueued values is not empty after dequeuing only one.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        _ = q.dequeue()
        self.assertFalse(q.is_empty())

   
    # """
    # Size
    # """

    def test_size0(self):
        """
        A queue is initially empty.
        """
        q = Queue()
        self.assertTrue(q.is_empty())


    def test_dequeue_from_an_empty_queue(self):  
        """
        Dequeueing from an empty queue raises ValueError. The size of the queue 
        remains 0
        """
        q = Queue()
        try:
            q.dequeue()
            self.fail("Did not raise an Exception")
        except ValueError:
            self.assertEqual(0, q.size())

    def test_size_after_enqueues(self):
        """
        Enqueueing a values increases the number of items in the queue.
        """
        q = Queue()
        q.enqueue('fee')
        self.assertEqual(1, q.size())
        q.enqueue('fi')
        self.assertEqual(2, q.size())
        q.enqueue('fo')
        self.assertEqual(3, q.size())
        q.enqueue('fum')
        self.assertEqual(4, q.size())

    def test_size_after_dequeues(self):  
        """
        Dequeueing a values increases the number of items in the queue.
        """
        q = Queue()
        q.enqueue('fee')
        q.enqueue('fi')
        q.enqueue('fo')
        q.enqueue('fum')
        self.assertEqual(4, q.size())
        q.dequeue()
        self.assertEqual(3, q.size())
        q.dequeue()
        self.assertEqual(2, q.size())
        q.dequeue()
        self.assertEqual(1, q.size())
        q.dequeue()
        self.assertEqual(0, q.size())

    def test_dequeue_from_an_empty_queue(self):  
        """
        Dequeueing from an empty queue raises an exception
        """
        q = Queue()
        try:
            q.dequeue()
            self.fail("Did not raise an Exception")
        except Exception:
            self.assertEqual(0, q.size())

    # """
    # Algorithmic complexity
    # """

    # def test_enqueue_efficiency(self):
    #     """
    #     Enqueing a value is always O(1).
    #     """
    #     time_samples = []
    #     for _ in range(0, 1000):
    #         q = Queue()
    #         start_time = time.time()
    #         q.enqueue('fake')
    #         end_time = time.time()
    #         time_samples.append(end_time - start_time)
    #     small_average_enqueue_time = sum(time_samples) / float(len(time_samples))

    #     large_queue = Queue()
    #     for _ in range(0, 1000000):
    #         large_queue.enqueue('fake')
    #     large_time_samples = []
    #     for _ in range(0, 1000):
    #         start_time = time.time()
    #         large_queue.enqueue('fake')
    #         end_time = time.time()
    #         large_time_samples.append(end_time - start_time)
    #     large_average_enqueue_time = sum(large_time_samples) / float(len(large_time_samples))
    #     self.assertAlmostEqual(small_average_enqueue_time, large_average_enqueue_time, delta=small_average_enqueue_time)

    def test_dequeue_efficiency(self):
        """
        Dequeuing a value is always O(1).
        """
        time_samples = []
        for _ in range(0, 1000):
            q = Queue()
            q.enqueue('fake')
            start_time = time.time()
            q.dequeue()
            end_time = time.time()
            time_samples.append(end_time - start_time)
        small_average_dequeue_time = sum(time_samples) / float(len(time_samples))

        large_queue = Queue()
        for _ in range(0, 1000000):
            large_queue.enqueue('fake')
        large_time_samples = []
        for _ in range(0, 1000):
            start_time = time.time()
            large_queue.dequeue()
            end_time = time.time()
            large_time_samples.append(end_time - start_time)
        large_average_dequeue_time = sum(large_time_samples) / float(len(large_time_samples))
        self.assertAlmostEqual(small_average_dequeue_time, large_average_dequeue_time, delta=small_average_dequeue_time)


def fake_value():
    return f"FAKE {time.time()}"

if __name__ == '__main__':
    unittest.main()
