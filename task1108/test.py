import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_case1(self):
        ip = "1.1.1.1"
        expected = "1[.]1[.]1[.]1"
        self.assertEqual(Solution().defangIPaddr(ip), expected,
                         f'incorrect result for ip: {ip}, expected: {expected}')

    def test_case2(self):
        ip = "255.100.50.0"
        expected = "255[.]100[.]50[.]0"
        self.assertEqual(Solution().defangIPaddr(ip), expected,
                         f'incorrect result for ip: {ip}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
