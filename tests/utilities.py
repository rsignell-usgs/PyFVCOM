import numpy.testing as test
import numpy as np

from datetime import datetime
from netCDF4 import num2date, date2num

from unittest import TestCase

from PyFVCOM.utilities import *

class StatsToolsTest(TestCase):

    def setUp(self):
        """ Make a couple of time series """
        start = date2num(datetime.strptime('2010-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'), units='days since 2010-01-01 00:00:00')
        end = date2num(datetime.strptime('2010-02-01 00:00:00', '%Y-%m-%d %H:%M:%S'), units='days since 2010-01-01 00:00:00')
        time = np.arange(start, end, 1/24/4)
        self.time = num2date(time, units='days since 2010-01-01 00:00:00')
        self.signal1 = np.sin(time) + np.cos(time)
        self.signal2 = np.cos(time) + np.tan(time)

    def test_fix_range(self):
        target_min, target_max = -100, 100
        scaled_signal = fix_range(self.signal1, target_min, target_max)
        test.assert_equal(scaled_signal.min(), target_min)
        test.assert_equal(scaled_signal.max(), target_max)