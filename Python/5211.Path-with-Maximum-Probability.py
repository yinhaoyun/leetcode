from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # print("maxProbability:", edges, succProb)
        node_max = max([max(a, b) for a, b in edges])
        if end > node_max:
            return 0
        dp = [0] * (max(node_max, end) + 1)
        dp[start] = 1
        map_prob = dict()

        for i, (a,b) in enumerate(edges):
            if map_prob.get(a) is None:
                map_prob[a] = []
            if map_prob.get(b) is None:
                map_prob[b] = []
            map_prob[a].append((b, succProb[i]))
            map_prob[b].append((a, succProb[i]))
        # print(map_prob)

        next_search = set()
        next_search.add(start)
        count = 0
        while len(next_search) > 0:
            # print("count = %d, next_search= %s" % (count, next_search))
            search = next_search.pop()
            if map_prob.get(search) is None:
                continue
            for (other, prob) in map_prob[search]:
                if dp[search] * prob > dp[other]:
                    dp[other] = dp[search] * prob  # Update!
                    # print(dp)
                    next_search.add(other)
            count += 1
        return dp[end]


s = Solution()
print(s.maxProbability(n=3, edges=[[0, 1], [1, 2], [0, 2]], succProb=[0.5, 0.5, 0.2], start=0, end=2))  # 0.25000
print(s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2))  # 0.30000
print(s.maxProbability(n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2))  # 0.00000
print(s.maxProbability(n = 3, edges = [[0,1],[1,2],[0,2],[1,3],[2,3]], succProb = [0.5,0.5,0.3, 0.2, 0.2], start = 0, end = 3))  # 0.30000
print(s.maxProbability(n=3, edges=[[0,1],[1,2],[0,2]], succProb=[0.5,0.5,0.2],start=0,end=2))  # 0.25