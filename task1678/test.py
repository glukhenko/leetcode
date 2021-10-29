import unittest
from task import Solution


class TestTask(unittest.TestCase):

    def test_case1(self):
        command = 'G()(al)'
        expected = 'Goal'
        self.assertEqual(Solution().interpret(command), expected,
                         f'incorrect result for command: {command}, expected: {expected}')

    def test_case2(self):
        command = 'G()()()()(al)'
        expected = 'Gooooal'
        self.assertEqual(Solution().interpret(command), expected,
                         f'incorrect result for command: {command}, expected: {expected}')

    def test_case3(self):
        command = '(al)G(al)()()G'
        expected = 'alGalooG'
        self.assertEqual(Solution().interpret(command), expected,
                         f'incorrect result for command: {command}, expected: {expected}')



if __name__ == '__main__':
    unittest.main()
