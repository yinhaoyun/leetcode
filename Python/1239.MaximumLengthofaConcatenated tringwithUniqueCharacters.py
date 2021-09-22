from typing import List


class Solution:
    # shortest
    def maxLength(self, arr: List[str]) -> int:
        best = 0
        result = [0]
        arr_i = [sum(1 << (ord(c) - ord('a')) for c in word) for word in arr if len(word) == len(set(word))]

        for word_i in arr_i:
            for i in range(len(result)):
                if word_i & result[i]:
                    continue
                new_res = word_i | result[i]
                result.append(new_res)
                best = max(best, bin(new_res).count("1"))
        return best

    def maxLength_readable(self, arr: List[str]) -> int:
        best = 0
        result = [0]

        arr = [word for word in arr if len(word) == len(set(word))]
        def word_to_int(word: str) -> int:
            return sum(1 << (ord(c) - ord('a')) for c in word)
        arr_i = [word_to_int(word) for word in arr]

        for word_i in arr_i:
            for i in range(len(result)):
                if word_i & result[i]:
                    continue
                new_res = word_i | result[i]
                result.append(new_res)
                best = max(best, bin(new_res).count("1"))
        return best


    def maxLength_simple(self, arr: List[str]) -> int:
        result = [""]
        best = 0
        for word in arr:
            for i in range(len(result)):
                new_res = result[i] + word
                if len(new_res) != len(set(new_res)):
                    continue
                result.append(new_res)
                best = max(best, len(new_res))
        return best


if __name__ == "__main__":
    s = Solution()
    print(s.maxLength(["un","iq","ue"])) # 4
    print(s.maxLength(["cha","r","act","ers"])) # 6
    print(s.maxLength(["yy","bkhwmpbiisbldzknpm"])) # 0