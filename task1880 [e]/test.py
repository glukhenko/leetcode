import unittest

from .task import Solution

class TestTask(unittest.TestCase):

    def test_ok(self):
        first_word = 'acb'
        second_word = 'cba'
        target_word = 'cdb'
        self.assertEqual(Solution().isSumEqual(first_word, second_word, target_word), True,
                         f'incorrect result for first_word: {first_word}, second_word: {second_word} '
                         f'target_word: {target_word}, expected: True')

    def test_ok2(self):
        first_word = 'aaa'
        second_word = 'a'
        target_word = 'aaaa'
        self.assertEqual(Solution().isSumEqual(first_word, second_word, target_word), True,
                         f'incorrect result for first_word: {first_word}, second_word: {second_word} '
                         f'target_word: {target_word}, expected: True')


    def test_ok3(self):
        first_word = 'j'
        second_word = 'j'
        target_word = 'bi'
        self.assertEqual(Solution().isSumEqual(first_word, second_word, target_word), True,
                         f'incorrect result for first_word: {first_word}, second_word: {second_word} '
                         f'target_word: {target_word}, expected: True')

    def test_fail(self):
        first_word = 'aaa'
        second_word = 'a'
        target_word = 'aab'
        self.assertEqual(Solution().isSumEqual(first_word, second_word, target_word), False,
                         f'incorrect result for first_word: {first_word}, second_word: {second_word} '
                         f'target_word: {target_word}, expected: False')

if __name__ == '__main__':
    unittest.main()