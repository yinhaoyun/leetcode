from typing import List


# https://leetcode.com/problems/partition-labels/
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        ends = {c: i for i, c in enumerate(S)}
        cur, cur_set, out = 0, set(), [0]

        for i, c in enumerate(S):
            cur_set.add(c)
            if ends[c] == i:
                cur_set.remove(c)
            if len(cur_set) == 0:
                out.append(i + 1)

        return [y - x for x, y in zip(out[:-1], out[1:])]


if __name__ == "__main__":
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))  # [9, 7, 8]