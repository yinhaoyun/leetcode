class Solution(object):
    def repeatedNTimes(self, A):
        for k in range(1, 4):
            for i in range(len(A) - k):
                print(k, i)
                if A[i] == A[i+k]:
                    return A[i]


if __name__ == "__main__":
    s = Solution()
    print(s.repeatedNTimes([1,2,3,3])) # 3
    print(s.repeatedNTimes([2,1,2,5,3,2])) # 2
    print(s.repeatedNTimes([5,1,5,2,5,3,5,4])) # 5