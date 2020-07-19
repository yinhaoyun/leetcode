class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]


s = Solution()
print(s.addBinary(a="11", b="1"))  # 100
print(s.addBinary(a="1010", b="1011"))  # 10101
