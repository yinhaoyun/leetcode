class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # print("isPowerOfFour: ", num)
        if num <= 0:
            return False
        while (num & 0x03) == 0:
            num >>= 2
            # print("shift:", num)
        return num == 1


s = Solution()

for i in range(5):
    print(i)
    print(s.isPowerOfFour(4**i))  # True

for i in range(5):
    print(i)
    print(s.isPowerOfFour(4**i-1))
    print(s.isPowerOfFour(4**i+1))