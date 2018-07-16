import unittest
def find_repeat(the_list):
    a=1;b=len(the_list)-1
    while a<b:
        midpoint=a+((b-a)/2)
        al, bl=a,midpoint
        au,bu= midpoint+1,b
        c=0
        for i in the_list:
            if i>=al and i<=bl:
                c+= 1
        d=(bl-al+1)
        if c>d:
            a,b=al,bl
        else:
            a,b=au,bu
    return a
# Tests
class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)