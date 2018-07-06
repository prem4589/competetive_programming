import unittest
def is_valid(code):
    lis = []
    for i in code:
        if(i=='(' or i=='[' or i=='{'):
            lis.append(i)
        else:
            if(len(lis)>0):
                check = lis.pop()
                if(ord(i)-ord(check)!=1 and ord(i)-ord(check)!=2 ):
                    return False
            else:
                return False
    if(len(lis)==0):
        return True
    else:
        False
# Tests
class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)