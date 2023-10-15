from typing import List, Set, Tuple
import unittest

# from .task import Solution
from work_space.task import Solution


class TestTask(unittest.TestCase):

    def __converter(self, l: List[List[int]]) -> Set[Tuple[int]]:
        return set(map(lambda items: tuple(sorted(tuple(items))), l))

    def __get_diff(self, r: List[List[int]], er: List[List[int]]):
        r_set = self.__converter(r)
        er_set = self.__converter(er)
        cross_set = r_set & er_set
        extra_result = r_set - cross_set
        not_enough = er_set - cross_set
        print(f'extra_result contain: {extra_result}')
        print(f'not_enough contain: {not_enough}')


    def test_case1(self):
        nums = [-1, 0, 1, 2, -1, -4]
        expected = [[-1, -1, 2], [-1, 0, 1]]
        result = Solution().threeSum(nums)
        is_same_result = self.__converter(result) == self.__converter(expected)
        self.assertTrue(is_same_result, f'bad result: {result}, expected: {expected}')

    def test_case2(self):
        nums = [0, 1, 1]
        expected = []
        result = Solution().threeSum(nums)
        is_same_result = self.__converter(result) == self.__converter(expected)
        self.assertTrue(is_same_result, f'bad result: {result}, expected: {expected}')

    def test_case3(self):
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        result = Solution().threeSum(nums)
        is_same_result = self.__converter(result) == self.__converter(expected)
        self.assertTrue(is_same_result, f'bad result: {result}, expected: {expected}')

    def test_case4(self):
        nums = [1, 2, -2, -1]
        expected = []
        result = Solution().threeSum(nums)
        is_same_result = self.__converter(result) == self.__converter(expected)
        self.assertTrue(is_same_result, f'bad result: {result}, expected: {expected}')

    def test_case5(self):
        nums = [34, 55, 79, 28, 46, 33, 2, 48, 31, -3, 84, 71, 52, -3, 93, 15, 21, -43, 57, -6, 86, 56, 94, 74, 83, -14,
                28, -66, 46, -49, 62, -11, 43, 65, 77, 12, 47, 61, 26, 1, 13, 29, 55, -82, 76, 26, 15, -29, 36, -29, 10,
                -70, 69, 17, 49]
        expected = [[-82, -11, 93], [-82, 13, 69], [-82, 17, 65], [-82, 21, 61], [-82, 26, 56], [-82, 33, 49],
                    [-82, 34, 48], [-82, 36, 46], [-70, -14, 84], [-70, -6, 76], [-70, 1, 69], [-70, 13, 57],
                    [-70, 15, 55], [-70, 21, 49], [-70, 34, 36], [-66, -11, 77], [-66, -3, 69], [-66, 1, 65],
                    [-66, 10, 56], [-66, 17, 49], [-49, -6, 55], [-49, -3, 52], [-49, 1, 48], [-49, 2, 47],
                    [-49, 13, 36], [-49, 15, 34], [-49, 21, 28], [-43, -14, 57], [-43, -6, 49], [-43, -3, 46],
                    [-43, 10, 33], [-43, 12, 31], [-43, 15, 28], [-43, 17, 26], [-29, -14, 43], [-29, 1, 28],
                    [-29, 12, 17], [-14, -3, 17], [-14, 1, 13], [-14, 2, 12], [-11, -6, 17], [-11, 1, 10], [-3, 1, 2]]
        temp = [[-82, -11, 93], [-82, 13, 69], [-82, 17, 65], [-82, 21, 61], [-82, 26, 56], [-82, 33, 49],
                [-82, 34, 48], [-82, 36, 46], [-70, -14, 84], [-70, -6, 76], [-70, 1, 69], [-70, 13, 57], [-70, 15, 55],
                [-70, 15, 55], [-70, 21, 49], [-70, 34, 36], [-66, -11, 77], [-66, -3, 69], [-66, 1, 65], [-66, 10, 56],
                [-66, 17, 49], [-49, -6, 55], [-49, -3, 52], [-49, 1, 48], [-49, 2, 47], [-49, 13, 36], [-49, 15, 34],
                [-49, 21, 28], [-49, 21, 28], [-43, -14, 57], [-43, -6, 49], [-43, -3, 46], [-43, 10, 33],
                [-43, 12, 31], [-43, 15, 28], [-43, 15, 28], [-43, 17, 26], [-29, -14, 43], [-29, 1, 28], [-29, 12, 17],
                [-14, -3, 17], [-14, 1, 13], [-14, 2, 12], [-11, -6, 17], [-11, 1, 10], [-3, 1, 2]]

        result = Solution().threeSum(nums)
        print(result)
        # self.__get_diff(result, expected)
        # is_same_result = self.__converter(result) == self.__converter(expected)
        is_same_result = result == expected

        for item, expected_item in zip(result, expected):
            assert item == expected_item, f'{item} != {expected_item}'

        self.assertTrue(is_same_result, f'bad result: {result}, expected: {expected}')


if __name__ == '__main__':
    unittest.main()
