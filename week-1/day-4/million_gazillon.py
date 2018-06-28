import unittest
class Trie(object):
    def __init__(self):
        self.root_node = {}
    def check(self, word):
        current = self.root_node
        check_new_word = False 
        for char in word:
            if char not in current:
                check_new_word = True
                current[char] = {}
            current = current[char]           
        if "i" not in current:
            check_new_word = True
            current["i"] = {}
        return check_new_word
# Tests
class Test(unittest.TestCase):

    def test_trie_usage(self):
        trie = Trie()

        result = trie.check('catch')
        self.assertTrue(result, msg='new word 1')

        result = trie.check('cakes')
        self.assertTrue(result, msg='new word 2')

        result = trie.check('cake')
        self.assertTrue(result, msg='prefix of existing word')

        result = trie.check('cake')
        self.assertFalse(result, msg='word already present')

        result = trie.check('caked')
        self.assertTrue(result, msg='new word 3')

        result = trie.check('catch')
        self.assertFalse(result, msg='all words still present')

        result = trie.check('')
        self.assertTrue(result, msg='empty word')

        result = trie.check('')
        self.assertFalse(result, msg='empty word present')
unittest.main(verbosity=2)