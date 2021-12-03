# https://leetcode.com/problems/reverse-words-in-a-string-iii/


class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    expected = "s'teL ekat edoCteeL tsetnoc"
    result = Solution().reverseWords(s)
    print(f'result: {result}')
