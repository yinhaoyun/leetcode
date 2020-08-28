import random


class Solution:
    def rand10(self):
        return sum([rand7() for _ in range(7)]) % 10 + 1


def rand7():
    return random.randint(1, 7)


if __name__ == "__main__":
    s = Solution()
    for _ in range(10):
        print(s.rand10())
