import unittest


def find_rotation_point(words):
    index = 0
    n = len(words)
    if n > 1:
        left = 0
        right = n- 1
        while (right - left) > 1:
            if words[left] > words[right]:
                nexttry = int((left + right) // 2.0)
                if words[nexttry] > words[right]:
                    left = nexttry
                else:
                    right = nexttry
            else:
                return left

        if words[left] <= words[right]:
            index = left
        else:
            index = right
    return index
# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)