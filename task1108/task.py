from typing import List

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

if __name__ == '__main__':
    ip = "1.1.1.1"
    expected = "1[.]1[.]1[.]1"
    Solution().defangIPaddr(ip)

