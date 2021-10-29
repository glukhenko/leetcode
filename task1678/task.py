from helpers.base_tree import TreeNode, BaseTree
from typing import List


class Solution:
    def interpret(self, command: str) -> str:
        dictionary = {
            'G': 'G',
            '()': 'o',
            '(al)': 'al',
        }
        result = ''
        temp = ''
        for char in command:
            temp += char
            if temp in dictionary:
                result += dictionary.get(temp)
                temp = ''

        return result

if __name__ == '__main__':
    command = 'G()(al)'
    expected = 'Goal'
    print(Solution().interpret(command))
