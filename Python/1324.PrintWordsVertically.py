from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        strings = s.split(" ")
        max_len = max([len(s) for s in strings])
        res = [""] * max_len
        for i in range(max_len):
            for j in strings:
                try:
                    res[i] = res[i] + j[i]
                except IndexError:
                    res[i] = res[i] + " "
        res = [s.rstrip() for s in res]
        return res

s = Solution()
print(s.printVertically("HOW ARE YOU"))  # ["HAY","ORO","WEU"]
print(s.printVertically("TO BE OR NOT TO BE"))  # ["TBONTB","OEROOE","   T"]
print(s.printVertically("CONTEST IS COMING"))  # ["CIC","OSO","N M","T I","E N","S G","T"]