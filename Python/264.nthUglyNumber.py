class Solution:
    def nthUglyNumber(self, n: int) -> int:
        l2 = [2]
        l3 = [3]
        l5 = [5]
        ugly_nums = [1]
        count = 1
        while count != n:
            v2 = l2[0]
            v3 = l3[0]
            v5 = l5[0]
            count += 1
            if v2 < v3:
                if v2 < v5:
                    del l2[0]
                    next_ugly = v2
                else:
                    del l5[0]
                    next_ugly = v5
            else:
                if v3 < v5:
                    del l3[0]
                    next_ugly = v3
                else:
                    del l5[0]
                    next_ugly = v5

            if next_ugly * 2 not in l3 and next_ugly * 2 not in l5:
                l2.append(next_ugly * 2)
            if next_ugly * 3 not in l2 and next_ugly * 3 not in l5:
                l3.append(next_ugly * 3)
            if next_ugly * 5 not in l2 and next_ugly * 5 not in l3:
                l5.append(next_ugly * 5)
            ugly_nums.append(next_ugly)
            print(ugly_nums, l2, l3, l5)
        return ugly_nums[n-1]

s = Solution()
print(s.nthUglyNumber(n = 10))  # 12