def check(l):
    mini =  l[0]
    maxi = l[1]-l[0]
    for i in range(1,len(l)):
        temp = l[i]-mini
        maxi = max(temp,maxi)
        mini = min(mini,l[i])
    return maxi
# Test cases
import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = check([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = check([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = check([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = check([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = check([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_one_price_raises_error(self):
        with self.assertRaises(Exception):
            check([1])

    def test_empty_list_raises_error(self):
        with self.assertRaises(Exception):
            check([])

unittest.main(verbosity=2)
