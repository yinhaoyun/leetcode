import collections


"""
https://leetcode.com/contest/biweekly-contest-32/problems/can-convert-string-in-k-moves/
"""
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        shifts = [abs(ord(c1) - ord(c2)) for c1, c2 in zip(s,t)]  # 26 alphas: -25~25

        if len([m for m in shifts if m != 0]) > k:
            return False

        # normalize
        print(shifts)
        ALPHA_NUM = 26
        ALPHA_NUM_MOD = ALPHA_NUM / 2
        shifts = [m if m <= ALPHA_NUM_MOD else ALPHA_NUM - m for m in shifts if m != 0]
        # shifts.sort()
        print("normalize:", shifts)  # all <=13
        shifts_count = collections.Counter(shifts)
        print(shifts_count)
        # k = min(25, k)
        max_move_found = k // ALPHA_NUM_MOD
        mod_move = k % ALPHA_NUM_MOD
        print(max_move_found, mod_move)
        for shift, count in shifts_count.items():
            #calc able move for current move
            print("check: ", shift, count)
            if shift > mod_move:
                if count > max_move_found:
                    return False
            else:
                if count > max_move_found + 1:
                    return False
        return True



s = Solution()
# print(s.canConvertString(s = "input", t = "ouput", k = 9))  # True
print(s.canConvertString(s = "abc", t = "bcd", k = 10))  # False
# print(s.canConvertString(s = "aab", t = "bbb", k = 27))  # True
# print(s.canConvertString(s = "abcd", t = "zyxw", k = 3))  # False
# print(s.canConvertString(s = "abcd", t = "zyxw", k = 4))  # False
# print(s.canConvertString("atmtxzjkz", "tvbtjhvjd", 35))  # False
# print(s.canConvertString("smgzrbq", "npotkmy", 23))  # False
# print(s.canConvertString("abcdefghijklmnopqrstuvwxyz", "aaaaaaaaaaaaaaaaaaaaaaaaaa", 25))