class SimpleTrie:
    def __init__(self):
        self.tries = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        # print("insert:", word)
        cur = self
        for c in word:
            cur = cur.tries.setdefault(c, SimpleTrie())
        cur.is_end = True

    def search(self, word: str) -> bool:
        # print("search:", word)
        if len(word) == 0:
            return self.is_end
        if word[0] in self.tries:
            # print(word[0], self.tries[word[0]])
            return self.tries[word[0]].search(word[1:])
        return False

    def startsWith(self, prefix: str) -> bool:
        # print("startsWith:", prefix)
        if len(prefix) == 0:
            return True
        return prefix[0] in self.tries and self.tries[prefix[0]].startsWith(prefix[1:])


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tries = {}

    def insert(self, word: str) -> None:
        self.tries.setdefault(len(word), SimpleTrie()).insert(word)

    def search(self, word: str) -> bool:
        if self.tries.get(len(word)) is None:
            return False
        return self.tries[len(word)].search(word)

    def startsWith(self, prefix: str) -> bool:
        for trie in self.tries.values():
            if trie.startsWith(prefix):
                return True
        return False


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))  # returns true
print(trie.search("app"))  # returns false
print(trie.startsWith("app"))  # returns true
print(trie.insert("app"))
print(trie.search("app"))  # returns true