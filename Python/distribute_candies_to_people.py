from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        dist = [0] * num_people
        i = 0
        while candies > 0:
            dist[i % num_people] += min(candies, i + 1)
            candies -= (i + 1)
            i += 1
        return dist


if __name__ == '__main__':
    s = Solution()
    print(s.distributeCandies(candies = 7, num_people = 4))  # [1,2,3,1]
    print(s.distributeCandies(candies = 10, num_people = 3))  # [5,2,3]
