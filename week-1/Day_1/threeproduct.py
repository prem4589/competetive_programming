import unittest


def pro3(array):
    highest_number = max(array[0], array[1])
    lowest_number = min(array[0], array[1])

    pro2 = array[0]* array[1]
    lpro2 = array[0]* array[1]

    pro3 = array[0]* array[1] * array[2]

    for i in xrange(2, len(list_of_ints)):
        current = list_of_ints[i]
        pro3 = max(pro3,
                                   current * pro2,
                                   current * lpro2)
        pro2 = max(pro2,
                                   current * highest,
                                   current * lowest)

        lpro2 = min(lpro2,
                                  current * highest,
                                  current * lowest)
        highest = max(highest, current)
        lowest = min(lowest, current
	return pro3
# Tests

class Test(unittest.TestCase):

    def test_short_list(self):
        actual = pro3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = pro3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = pro3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = pro3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = pro3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            pro3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            pro3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            pro3([1, 1])


unittest.main(verbosity=2)
