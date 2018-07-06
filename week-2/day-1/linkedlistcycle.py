import unittest
def has_cycle(node):
    point1=node
    point2=node
    while(point1!=None and point2!=None and point2.next!=None ):
        point1=point1.next
        point2=point2.next.next
        if(point1==point2):
            return True
    return False
# Tests
class Test(unittest.TestCase):
    class LinkedListNode(object):
        def __init__(self, value, next=None):
            self.value = value
            self.next  = next
    def test_linked_list_with_no_cycle(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        result = has_cycle(first)
        self.assertFalse(result)

    def test_cycle_loops_to_beginning(self):
        fourth = Test.LinkedListNode(4)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fourth.next = first
        result = has_cycle(first)
        self.assertTrue(result)

    def test_cycle_loops_to_middle(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = third
        result = has_cycle(first)
        self.assertTrue(result)

    def test_two_node_cyle_at_end(self):
        fifth = Test.LinkedListNode(5)
        fourth = Test.LinkedListNode(4, fifth)
        third = Test.LinkedListNode(3, fourth)
        second = Test.LinkedListNode(2, third)
        first = Test.LinkedListNode(1, second)
        fifth.next = fourth
        result = has_cycle(first)
        self.assertTrue(result)

    def test_empty_list(self):
        result = has_cycle(None)
        self.assertFalse(result)

    def test_one_element_linked_list_no_cycle(self):
        first = Test.LinkedListNode(1)
        result = has_cycle(first)
        self.assertFalse(result)

    def test_one_element_linked_list_cycle(self):
        first = Test.LinkedListNode(1)
        first.next = first
        result = has_cycle(first)
        self.assertTrue(result)
unittest.main(verbosity=2)