# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/


class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        for bit in f'{num:b}':
            steps += 1 + int(bit)
        return steps - 1

    def numberOfStepsSlow(self, num: int) -> int:
        b_num = f'{num:b}'
        return len(b_num) - 1 + b_num.count('1')

if __name__ == '__main__':
    num = 14
    expected = 6
    Solution().numberOfSteps(num)
