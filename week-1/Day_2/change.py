import unittest

def check(amount, values):
	n=amount
	m=len(values)
	coins = values
	dp = [1]+[0]*n
	for i in range(m): 
	    for j in range(coins[i], n+1):
	    	dp[j]+=dp[j-coins[i]]
	return dp[-1]
#---------------------------------------------------------------------------------------------
class Test(unittest.TestCase):

    def test_sample_input(self):
        actual = check(4, (1, 2, 3))
        expected = 4
        self.assertEqual(actual, expected)

    def test_one_way_to_make_zero_cents(self):
        actual = check(0, (1, 2))
        expected = 1
        self.assertEqual(actual, expected)

    def test_no_ways_if_no_coins(self):
        actual = check(1, ())
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_coin_value(self):
        actual = check(5, (25, 50))
        expected = 0
        self.assertEqual(actual, expected)

    def test_big_target_amount(self):
        actual = check(50, (5, 10))
        expected = 6
        self.assertEqual(actual, expected)

    def test_change_for_one_dollar(self):
        actual = check(100, (1, 5, 10, 25, 50))
        expected = 292
        self.assertEqual(actual, expected)
unittest.main(verbosity=2)
