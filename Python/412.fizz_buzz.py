from typing import List


# https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ["FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(1, n + 1)]


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(15))
