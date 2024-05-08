import unittest
from train_api import *

class TestTrainApi(unittest.TestCase):
    #Tests range of values to capture edge cases, realistically we wont encounter anything like this
    def test_calculate_train_emissions_standardized(self):
        self.assertEqual(35,calculate_train_emissions_standardized(1,35))

        self.assertEqual(0, calculate_train_emissions_standardized(0, 35))

        self.assertEqual(200, calculate_train_emissions_standardized(10, 20))

        self.assertEqual(220, calculate_train_emissions_standardized(5.5, 40))

        self.assertEqual(137.5, calculate_train_emissions_standardized(2.75, 50))

        self.assertEqual(0, calculate_train_emissions_standardized(100, 0))

if __name__ == '__main__':
    unittest.main()

