from typing import List


class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        # print("prerequisites", prerequisites)
        p_to_c = dict()  # prerequisite: course
        prerequisite_count = [0] * num_courses
        for c, p in prerequisites:
            if p_to_c.get(p) is None:
                p_to_c[p] = []
            p_to_c[p].append(c)
            prerequisite_count[c] += 1

        # print("p_to_c", p_to_c)
        # print("prerequisite_count", prerequisite_count)

        res = []
        q = []
        for c, p in enumerate(prerequisite_count):
            if p == 0:
                q.append(c)

        # print("init q = ", q)
        while len(q) != 0:
            p = q.pop()
            # print("p=", p)
            res.append(p)
            if p_to_c.get(p) is None:
                continue
            for c in p_to_c[p]:
                prerequisite_count[c] -= 1
                if prerequisite_count[c] == 0:
                    q.append(c)

        if len(res) != num_courses:
            res = []
        return res


s = Solution()
print(s.findOrder(2, [[1,0]]))  # [0,1]
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))  # [0,1,2,3] or [0,2,1,3]