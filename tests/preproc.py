import os
import tempfile

import numpy.testing as test
import numpy as np

from unittest import TestCase
from datetime import datetime
from dateutil.relativedelta import relativedelta

from PyFVCOM.preproc import Model
from PyFVCOM.grid import write_sms_mesh
from PyFVCOM.utilities import date_range


class PreProcessingTest(TestCase):

    def setUp(self):

        # Add a grid.
        self.lon, self.lat, self.h, self.triangles = _prep()

        self.start = datetime.strptime('2015-01-01', '%Y-%m-%d')
        self.end = datetime.strptime('2015-02-01', '%Y-%m-%d')

        self.grid = tempfile.NamedTemporaryFile(mode='w', suffix='.2dm', delete=False)
        self.sigma = tempfile.NamedTemporaryFile(mode='w', suffix='.dat', delete=False)
        with open(self.sigma.name, 'w') as sigma:
            sigma.write('NUMBER OF SIGMA LEVELS = 11\n')
            sigma.write('SIGMA COORDINATE TYPE = UNIFORM\n')
        write_sms_mesh(self.triangles, np.arange(len(self.lon)) + 1, self.lon, self.lat, self.h,
                       np.zeros(len(self.lon)), self.grid.name)
        self.model = Model(self.start, self.end, self.grid.name, native_coordinates='spherical')

    def tearDown(self):
        os.remove(self.grid.name)
        os.remove(self.sigma.name)

    def test_add_bed_roughness(self):
        self.model.add_bed_roughness(0.25)
        test.assert_equal(self.model.grid.roughness, np.ones(self.model.dims.nele) * 0.25)

    def test_sigma_gen(self):
        """ This is all sorts of wrong at the moment! """
        self.model.add_sigma_coordinates(self.sigma.name)
        sigma_levels = []
        single_result = np.array([0, -0.01083786, -0.02167571, -0.03251357, -0.04335143,
                                  -0.05418928, -0.04977951, -0.04536974, -0.04095997, -0.0365502,
                                  -0.03214043, -0.02773066, -0.02332089, -0.01891112, -0.01450135,
                                  -0.01009158, -0.00568181, -0.00127204, 0.00313773, 0.0075475,
                                  0.01195727, 0.01636704, 0.02077681, 0.02518658, 0.02959635,
                                  np.nan, np.nan, np.nan, np.nan, np.nan])
        for h in self.model.grid.h:
            sigma_levels.append(self.model._sigma_gen(30, 10, 10, 5, 5, [0.2] * 5, [0.2] * 5, h, 5))
        test.assert_almost_equal(np.asarray(sigma_levels[50]), single_result)

    def test_add_rivers(self):
        positions = [[-5, 50], [-8, 60]]
        names = ['river1', 'river2']
        times = date_range(self.start + relativedelta(days=-4), self.end + relativedelta(days=4))
        flux = np.ones((len(times), len(positions)))
        temperature = np.ones((len(times), len(positions))) * 15
        salinity = np.ones((len(times), len(positions))) * 30
        self.model.add_rivers(positions, names, times, flux, temperature, salinity)
        test.assert_equal(self.model.river.flux, flux)
        test.assert_equal(self.model.river.temperature, temperature)
        test.assert_equal(self.model.river.salinity, salinity)

    def test_add_probes(self):
        positions = [[-5, 50], [-8, 60]]
        names = ['probe1', 'probe2']
        variables = ['u', 'v', 't1']
        interval = 900
        # Need sigma coordinates for this.
        self.model.add_sigma_coordinates(self.sigma.name)
        self.model.add_probes(positions, names, variables, interval)
        test.assert_equal(self.model.probes.grid, [[8, 8, 67], [72, 72, 30]])
        test.assert_equal(self.model.probes.variables, [variables] * len(names))
        test.assert_equal(self.model.probes.interval, interval)


def _prep():
    """
    Make some input data (a grid and a time range).

    Returns
    -------
    lon, lat : np.ndarray
        Longitude and latitudes for the grid.
    h : np.ndarray
        Water depths.
    triangles : np.ndarray
        Triangulation table for the grid.

    Notes
    -----
    The triangulation is lifted from the matplotlib.triplot demo:
       https://matplotlib.org/examples/pylab_examples/triplot_demo.html

    """

    xy = np.asarray([
        [-0.101, 0.872], [-0.080, 0.883], [-0.069, 0.888], [-0.054, 0.890],
        [-0.045, 0.897], [-0.057, 0.895], [-0.073, 0.900], [-0.087, 0.898],
        [-0.090, 0.904], [-0.069, 0.907], [-0.069, 0.921], [-0.080, 0.919],
        [-0.073, 0.928], [-0.052, 0.930], [-0.048, 0.942], [-0.062, 0.949],
        [-0.054, 0.958], [-0.069, 0.954], [-0.087, 0.952], [-0.087, 0.959],
        [-0.080, 0.966], [-0.085, 0.973], [-0.087, 0.965], [-0.097, 0.965],
        [-0.097, 0.975], [-0.092, 0.984], [-0.101, 0.980], [-0.108, 0.980],
        [-0.104, 0.987], [-0.102, 0.993], [-0.115, 1.001], [-0.099, 0.996],
        [-0.101, 1.007], [-0.090, 1.010], [-0.087, 1.021], [-0.069, 1.021],
        [-0.052, 1.022], [-0.052, 1.017], [-0.069, 1.010], [-0.064, 1.005],
        [-0.048, 1.005], [-0.031, 1.005], [-0.031, 0.996], [-0.040, 0.987],
        [-0.045, 0.980], [-0.052, 0.975], [-0.040, 0.973], [-0.026, 0.968],
        [-0.020, 0.954], [-0.006, 0.947], [ 0.003, 0.935], [ 0.006, 0.926],
        [ 0.005, 0.921], [ 0.022, 0.923], [ 0.033, 0.912], [ 0.029, 0.905],
        [ 0.017, 0.900], [ 0.012, 0.895], [ 0.027, 0.893], [ 0.019, 0.886],
        [ 0.001, 0.883], [-0.012, 0.884], [-0.029, 0.883], [-0.038, 0.879],
        [-0.057, 0.881], [-0.062, 0.876], [-0.078, 0.876], [-0.087, 0.872],
        [-0.030, 0.907], [-0.007, 0.905], [-0.057, 0.916], [-0.025, 0.933],
        [-0.077, 0.990], [-0.059, 0.993]])
    lon = np.degrees(xy[:, 0])
    lat = np.degrees(xy[:, 1])
    triangles = np.asarray([
        [67, 66, 1], [65, 2, 66], [1, 66, 2], [64, 2, 65], [63, 3, 64],
        [60, 59, 57], [2, 64, 3], [3, 63, 4], [0, 67, 1], [62, 4, 63],
        [57, 59, 56], [59, 58, 56], [61, 60, 69], [57, 69, 60], [4, 62, 68],
        [6, 5, 9], [61, 68, 62], [69, 68, 61], [9, 5, 70], [6, 8, 7],
        [4, 70, 5], [8, 6, 9], [56, 69, 57], [69, 56, 52], [70, 10, 9],
        [54, 53, 55], [56, 55, 53], [68, 70, 4], [52, 56, 53], [11, 10, 12],
        [69, 71, 68], [68, 13, 70], [10, 70, 13], [51, 50, 52], [13, 68, 71],
        [52, 71, 69], [12, 10, 13], [71, 52, 50], [71, 14, 13], [50, 49, 71],
        [49, 48, 71], [14, 16, 15], [14, 71, 48], [17, 19, 18], [17, 20, 19],
        [48, 16, 14], [48, 47, 16], [47, 46, 16], [16, 46, 45], [23, 22, 24],
        [21, 24, 22], [17, 16, 45], [20, 17, 45], [21, 25, 24], [27, 26, 28],
        [20, 72, 21], [25, 21, 72], [45, 72, 20], [25, 28, 26], [44, 73, 45],
        [72, 45, 73], [28, 25, 29], [29, 25, 31], [43, 73, 44], [73, 43, 40],
        [72, 73, 39], [72, 31, 25], [42, 40, 43], [31, 30, 29], [39, 73, 40],
        [42, 41, 40], [72, 33, 31], [32, 31, 33], [39, 38, 72], [33, 72, 38],
        [33, 38, 34], [37, 35, 38], [34, 38, 35], [35, 37, 36]])

    h = (np.sin(lon) + np.cos(lat) + 1) * 100  # some made up depths.

    return lon, lat, h, triangles