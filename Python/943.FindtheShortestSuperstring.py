import copy
import itertools
import math
from typing import List


class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        N = len(words)
        g = [[0 for _ in range(N)] for _ in range(N)]
        for i, j in itertools.product(range(N), range(N)):
            if i == j:
                continue
            g[i][j] = self.find_cost(words[i], words[j])
        # print(g)

        def dfs(depth, cur_len) -> None:
            nonlocal best_path, best_len
            if cur_len >= best_len:
                return
            if depth == N:
                best_path = copy.copy(path)
                best_len = cur_len

            for j in range(N):
                if used[j]: continue
                used[j] = True
                path.append(j)
                dfs(depth + 1, len(words[j]) if depth == 0 else cur_len + g[path[-2]][j])
                path.pop()
                used[j] = False
            return

        best_path = []
        best_len = math.inf
        path = []
        used = [False] * N

        dfs(0, 0)
        print(best_len, best_path)
        ans = words[best_path[0]] +\
              "".join([words[p][-g[best_path[i]][p]:] for i, p in enumerate(best_path[1:])])
        return ans

    @staticmethod
    def find_cost(word1, word2) -> int:
        L1, L2 = len(word1), len(word2)
        for i in range(L1):
            overlap_len = L2 if L1 - i >= L2 else (L1 - i)
            if word1[i:i + overlap_len] == word2[:overlap_len]:
                return len(word2) - overlap_len
        return len(word2)


if __name__ == "__main__":
    s = Solution()
    print(s.shortestSuperstring(["alex", "loves", "leetcode"]))  # alexlovesleetcode
    print(s.shortestSuperstring(["catg", "ctaagt", "gcta", "ttca", "atgcatc"])) # gctaagttcatgcatc
    print(s.shortestSuperstring(["orugbsuuxowmhjh","zjyxzmpduthlsioor","qtxocgehmhfqnstl","tlrlcnnrsyryfrywuebq","hozjyxzmpduthlsio","hjhdmnqtxocgehm","mjhzwdudlnbfkjawqacf","hfqnstlrlcnnrsyryfry","yfrywuebqhvwewzmq","zzieemjhzwdudlnbfkj","nnrsyryfrywuebqhvw","acfgaihbhozjyxzmpdut"]))
