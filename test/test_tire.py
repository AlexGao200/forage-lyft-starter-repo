import unittest
from tire_models.carrigan_tire import *
from tire_models.octoprime_tire import *

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensors = [1, 1, 1, 1]
        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0.1, 0.1, 0.1, 0.1]
        tire = CarriganTire(sensors)
        self.assertFalse(tire.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        sensors = [1, 1, 1, 1]
        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        sensors = [0.1, 0.1, 0.1, 0.1]
        tire = OctoprimeTire(sensors)
        self.assertFalse(tire.needs_service())