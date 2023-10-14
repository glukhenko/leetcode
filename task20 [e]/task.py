# https://leetcode.com/problems/valid-parentheses/description/

class Solution:

    def __init__(self):
        self.brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
        }
        self.open_brackets = []

    def is_open_bracket(self, char: str):
        return char in self.brackets

    def is_close_bracket(self, char: str):
        return char in self.brackets.values()

    def is_valid_type_bracket(self, open_bracket: str, close_bracket: str):
        return self.brackets[open_bracket] == close_bracket

    def isValid(self, s: str) -> bool:
        for char in s:
            if self.is_open_bracket(char):
                self.open_brackets.append(char)
            else:
                if not self.open_brackets:
                    return False
                open_bracket = self.open_brackets.pop()
                if not self.is_valid_type_bracket(open_bracket, close_bracket=char):
                    return False

        return not bool(self.open_brackets)

if __name__ == '__main__':
    s = "()[]{}"
    expected = True
    result = Solution().isValid(s)
    assert result is expected, f'Bad result: {result}'
