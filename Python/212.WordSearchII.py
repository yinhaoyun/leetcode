from typing import List


class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True


class Solution:
    DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        ans = []
        for w in words:
            trie.insert(w)
        for y in range(len(board)):
            for x in range(len(board[0])):
                self.dfs(y, x, board, trie.root, "", ans)

        return ans

    def dfs(self, y, x, board, node: TrieNode, path, ans):
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or \
                board[y][x] not in node.children:
            return
        tmp, board[y][x] = board[y][x], "#"
        node = node.children[tmp]
        if node.is_end:
            ans.append(path+tmp)
            node.is_end = False

        for dy, dx in Solution.DIRS:
            self.dfs(y + dy, x + dx, board, node, path + tmp, ans)
        board[y][x] = tmp


if __name__ == "__main__":
    s = Solution()
    print(s.findWords(board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                      words=["oath", "pea", "eat", "rain"]))  # Output: ["eat","oath"]
    print(s.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]))  # []
