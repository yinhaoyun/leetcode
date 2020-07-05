class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        dist = 0
        while xor > 0:
            if xor & 0x01:
                dist+=1
            xor >>= 1
        return dist

s = Solution()
print(s.hammingDistance(1,4))
