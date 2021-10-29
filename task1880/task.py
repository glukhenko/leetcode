class Solution:
    def __init__(self):
        self.map_chars = self.__get_map_chars()

    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.word_to_num2(firstWord) + self.word_to_num2(secondWord) == self.word_to_num2(targetWord)

    def word_to_num(self, word: str):
        """Возвращает число по входному слову"""
        return int(''.join(self.map_chars.get(char) for char in word))

    def word_to_num2(self, word: str):
        """Возвращает число по входному слову"""
        return int(''.join(str(ord(char)-ord('a')) for char in word))

    def __get_map_chars(self):
        """Возвращает словарь симполов"""
        return {char: f'{i}' for i, char in enumerate('abcdefghij')}

if __name__ == '__main__':
    first_word = 'aaa'
    second_word = 'a'
    target_word = 'aab'
    Solution().isSumEqual(first_word, second_word, target_word)

