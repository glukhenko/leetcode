import unittest

from .task import ParkingSystem

class TestTask(unittest.TestCase):

    def test_case1(self):
        parking_slots = [1, 1, 0]
        parking = ParkingSystem(*parking_slots)
        result = [None]
        cars = (1, 2, 3, 1)
        for car in cars:
            result.append(parking.addCar(car))
        expected = [None, True, True, False, False]
        self.assertEqual(result, expected,
                         f'incorrect result for result: {result}, expected: {expected}')

if __name__ == '__main__':
    unittest.main()
