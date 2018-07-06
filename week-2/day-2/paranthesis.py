import unittest
def get_closing_paren(word, index):
    count = 0
    l = len(word)
    for i in range (index+1,l):
        if(word[i]=='('):
            count+=1;
        elif(word[i]==')'):
            if(count == 0):
                return i
            else:
                count-=1
    raise Exception
class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)
unittest.main(verbosity=2)