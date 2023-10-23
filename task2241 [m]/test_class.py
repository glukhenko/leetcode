import unittest
from typing import List

from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        operations = ["deposit", "withdraw", "deposit", "withdraw", "withdraw"]
        values = [[0, 0, 1, 2, 1], 600, [0, 1, 0, 1, 1], 600, 550]

        obj = ATM()
        result = [getattr(obj)(value) for operation, value in zip(operations, values)]
        expected = [None, None, [0, 0, 1, 0, 1], None, [-1], [0, 1, 0, 0, 1]]
        assert result == expected, f'Bad result: {result}, but expected: {expected}'


if __name__ == '__main__':
    unittest.main()
