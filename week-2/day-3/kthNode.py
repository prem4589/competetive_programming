import unittest
def check(k, head):
    # Return the kth to last node in the linked list
    a=0;co=1;b=head
    if(k==0):
        raise Exception
    while(head and head.next):
        co+=1
        head=head.next
        if a==k-1:
            b=b.next
        else:
            a+= 1          
    if(co<k):
        raise Exception
    return b
# Tests
class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = check(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = check(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = check(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_length(self):
        with self.assertRaises(Exception):
            check(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            check(0, self.first)
unittest.main(verbosity=2)