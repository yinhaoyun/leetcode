import collections
from typing import List


# TODO: Could Improve
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and len(trust) == 0:
            return 1
        trust_dic = collections.defaultdict(int)
        be_trust_dic = collections.defaultdict(int)
        for a, b in trust:
            trust_dic[a] = trust_dic[a] + 1
            be_trust_dic[b] = be_trust_dic[b] + 1
        # print(trust_dic)

        # Everybody (except for the town judge) trusts the town judge.
        candidate = [b for b, a in be_trust_dic.items() if a == N - 1]

        # The town judge trusts nobody.s
        candidate = [c for c in candidate if trust_dic[c] == 0]

        # print("candidate = ", candidate)
        if len(candidate) == 1:
            return candidate[0]
        else:
            return -1


s = Solution()
print(s.findJudge(N = 2, trust = [[1,2]]))  # 2
print(s.findJudge(N = 3, trust = [[1,3],[2,3]]))  # 3
print(s.findJudge(N = 3, trust = [[1,3],[2,3],[3,1]]))  # -1
print(s.findJudge(N = 3, trust = [[1,2],[2,3]]))  # -1
print(s.findJudge(N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]))  # 3
print(s.findJudge(1, []))  # 1