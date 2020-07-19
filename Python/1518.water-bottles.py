class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles > 0:
            mod_bottles = numBottles % numExchange
            numBottles = numBottles // numExchange
            if numBottles == 0:
                break
            res += numBottles
            numBottles += mod_bottles
        return res


s = Solution()
print(s.numWaterBottles(numBottles = 9, numExchange = 3))  # 13
print(s.numWaterBottles(numBottles = 15, numExchange = 4))  # 19