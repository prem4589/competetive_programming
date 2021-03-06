import unittest
class TemperatureTracker(object):    
    def __init__(self):
        self.temperature_array=[0]*200
        self.tempCount = 0
        self.temp_min =200
        self.max_var = -1
        self.total = 0
        self.average = None
        self.maxFreq = 0
        self.mode = None
    def get_max(self):
        max_var=self.max_var
        if max_var==-1:
            return None
        return max_var
    def get_minTemp(self):
        temp_min=self.temp_min
        if temp_min==200:
            return None
        return temp_min
    def insert(self, temperature):
        self.temperature_array[temperature]+=1
        self.tempCount+=1
        if temperature<self.temp_min:
            self.temp_min=temperature
        if temperature>self.max_var:
            self.max_var=temperature
        self.total+=temperature
        self.average=self.total/float(self.tempCount)
        if self.temperature_array[temperature]>self.maxFreq:
            self.maxFreq=self.temperature_array[temperature]
            self.mode=temperature
    def get_mean(self):
        return self.average
    def get_mode(self):
        return self.mode
# Tests
class Test(unittest.TestCase):

    def test_tracker_usage(self):
        tracker = TemperatureTracker()

        tracker.insert(50)
        msg = 'failed on first temp recorded'
        self.assertEqual(tracker.get_max(), 50, msg='max_var ' + msg)
        self.assertEqual(tracker.get_minTemp(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 50.0, msg='average ' + msg)
        self.assertEqual(tracker.get_mode(), 50, msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on higher temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max_var ' + msg)
        self.assertEqual(tracker.get_minTemp(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 65.0, msg='average ' + msg)
        self.assertIn(tracker.get_mode(), [50, 80], msg='mode ' + msg)

        tracker.insert(80)
        msg = 'failed on third temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max_var ' + msg)
        self.assertEqual(tracker.get_minTemp(), 50, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 70.0, msg='average ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)

        tracker.insert(30)
        msg = 'failed on lower temp recorded'
        self.assertEqual(tracker.get_max(), 80, msg='max_var ' + msg)
        self.assertEqual(tracker.get_minTemp(), 30, msg='min ' + msg)
        self.assertEqual(tracker.get_mean(), 60.0, msg='average ' + msg)
        self.assertEqual(tracker.get_mode(), 80, msg='mode ' + msg)
unittest.main(verbosity=2)
