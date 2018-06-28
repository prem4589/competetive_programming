import unittest


def merge_ranges(meetings):
    l=meetings
    l.sort()
    l1=[]
    t=-1
    count=0
    for i in range(len(l)-1):
        if(len(l[i])==0):
            l1.append((1,l[i+1][1]))
            continue
        if(l[i+1][0]<=l[i][1]):
            if(count==0):
                t=l[i][0]
                count+=1
            if(i==len(l)-2):
                if(l[i-count+1][1]>l[i+1][1]):
                    l1.append((l[i-count+1][0],l[i-count+1][1]))
                else:
                    l1.append((l[i-count+1][0],l[i+1][1]))
        else:
            if(l[i-count][0]==t):
                l1.append((l[i-count][0],l[i][1]))
                count=0
                t=-1
            else:
                if(i+2==len(l)):
                    l1.append(l[i])
                    l1.append(l[i+1])
                else:
                    l1.append(l[i])
    return l1


















# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(          ), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
