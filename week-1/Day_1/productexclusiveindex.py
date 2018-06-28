import unittest
def check(int_list):
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')
    x = [None] * len(int_list)
    pro = 1
    for i in range(len(int_list)):
        x[i] = pro
        pro *= int_list[i]
    pro = 1
    for i in range(len(int_list) - 1, -1, -1):
        x[i] *= pro
        pro *= int_list[i]

    return x
# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = check([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = check([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = check([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = check([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = check([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = check([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            check([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            check([1])


unittest.main(verbosity=2)
