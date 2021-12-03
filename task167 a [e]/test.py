import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        numbers = [2, 7, 11, 15]
        target = 9
        expected = [1, 2]
        self.assertEqual(Solution().twoSum(numbers, target), expected,
                         f'incorrect result for numbers: {numbers}, target: {target}, expected: {expected}')

    def test_case2(self):
        numbers = [2, 3, 4]
        target = 6
        expected = [1, 3]
        self.assertEqual(Solution().twoSum(numbers, target), expected,
                         f'incorrect result for numbers: {numbers}, target: {target}, expected: {expected}')

    def test_case3(self):
        numbers = [-1, 0]
        target = -1
        expected = [1,2]
        self.assertEqual(Solution().twoSum(numbers, target), expected,
                         f'incorrect result for numbers: {numbers}, target: {target}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
