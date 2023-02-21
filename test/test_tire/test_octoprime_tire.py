import unittest

from my_code.tires.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_numbers = [0.4, 0.9, 1, 0.9]
        tire = OctoprimeTire(sensor_numbers)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_numbers = [0, 0.4, 0.5, 0.4]
        tire = OctoprimeTire(sensor_numbers)
        self.assertFalse(tire.needs_service())
