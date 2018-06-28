import unittest
def contains(l, number):
    down=0
    top=len(l)
    while down<top:
        x=(down + top)//2
        y=l[x]     
        if y==number:
            return True
        if y>number:
            top=x-1
        else:
            down=x+1
    return False
# Tests
class Test(unittest.TestCase):

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)
    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)
    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)
    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)
    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)
    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)
    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)
    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)
unittest.main(verbosity=2)