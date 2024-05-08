import unittest
from carApi import *

class TestCarApi(unittest.TestCase):
    def test_miles_to_kilometers(self):
        #Have to use almost equal because were dealing with float
        self.assertAlmostEqual(miles_to_kilometers(1), 1.60934)
        self.assertAlmostEqual(miles_to_kilometers(10), 16.0934)
        self.assertAlmostEqual(miles_to_kilometers(100), 160.934)
        self.assertAlmostEqual(miles_to_kilometers(-1), -1.60934)
        self.assertAlmostEqual(miles_to_kilometers(-10), -16.0934)
        self.assertAlmostEqual(miles_to_kilometers(-100), -160.934)

    def test_gkm_to_gm(self):
        self.assertAlmostEqual(gkm_to_gm(1), 1.60934)
        self.assertAlmostEqual(gkm_to_gm(10), 16.0934)
        self.assertAlmostEqual(gkm_to_gm(100), 160.934)
        self.assertAlmostEqual(gkm_to_gm(0), 0.0)
        self.assertAlmostEqual(gkm_to_gm(-1), -1.60934)
        self.assertAlmostEqual(gkm_to_gm(-10), -16.0934)
        self.assertAlmostEqual(gkm_to_gm(-100), -160.934)

    #API works with my car, not publishing my licence plate online tho >:(
    def test_vehicle_enquiry(self):
        self.assertAlmostEqual(158,vehicle_enquiry(""))


        

if __name__ == '__main__':
    unittest.main()

