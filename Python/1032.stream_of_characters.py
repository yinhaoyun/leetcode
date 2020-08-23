import collections
from typing import List
from Python.data_structure.trie import Trie


# https://leetcode.com/problems/stream-of-characters/
# TODO: Implement a reverse trie solution
class StreamChecker:

    def __init__(self, words: List[str]):
        self.s = ''
        self.dic = collections.defaultdict(set)
        for w in words:
            self.dic[w[-1]].add(w)

    # Runtime: 1680 ms, faster than 30.06%
    def query(self, letter: str) -> bool:
        self.s += letter
        return any(self.s.endswith(w) for w in self.dic[letter])


if __name__ == "__main__":
    s = StreamChecker(["cd","f","kl"])
    for i in range(ord('a'), ord('l') + 1):
        print(chr(i), s.query(chr(i)))

    # s = StreamChecker(["ab","ba","aaab","abab","baa"])
    # queries = [["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]]
    # for w in queries:
    #     print(w[0], s.query(w[0]))
