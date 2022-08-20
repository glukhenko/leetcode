# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        count = 0
        chars = []

        for char in s:
            if char in chars:
                count = max(count, len(chars))
                index = chars.index(char)
                chars = chars[index + 1:]
            chars.append(char)
        count = max(count, len(chars))
        return count



if __name__ == '__main__':
    s = "abcabcbb"
    expected = 3
    result = Solution().lengthOfLongestSubstring(s)
    print(f'result: {result}')
