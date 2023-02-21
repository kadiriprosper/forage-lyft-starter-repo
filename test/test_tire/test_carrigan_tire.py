import unittest

from my_code.tires.carrigan_tire import CarriganTire


class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_numbers = [0, 0.4, 0.1, 0.9]
        tire = CarriganTire(sensor_numbers)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        sensor_numbers = [0, 0.4, 0.5, 0.8]
        tire = CarriganTire(sensor_numbers)
        self.assertFalse(tire.needs_service())
