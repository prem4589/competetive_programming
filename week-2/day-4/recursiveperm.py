import unittest
def get_permutations(string):
    if len(string) <= 1:
        return set([string])
    a=string[:-1]
    lastc=string[-1]
    p=get_permutations(a)
    perm=set()
    for i in p:
        for j in range(len(a) + 1):
            permut=(i[:j]+lastc+i[j:])
            perm.add(permut)
    return perm
# Tests
class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)