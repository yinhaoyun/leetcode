class Trie:
    def __init__(self):
        self.tries = {}
        self.is_end = False

    def insert(self, word: str) -> None:
        # print("insert:", word)
        cur = self
        for c in word:
            cur = cur.tries.setdefault(c, Trie())
        cur.is_end = True

    def search(self, word: str) -> bool:
        # print("search:", word)
        cur = self
        for c in word:
            if c in cur.tries:
                cur = cur.tries[c]
            else:
                return False
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        # print("startsWith:", prefix)
        cur = self
        for c in prefix:
            if c in cur.tries:
                cur = cur.tries[c]
            else:
                return False
        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))  # returns true
print(trie.search("app"))  # returns false
print(trie.startsWith("app"))  # returns true
trie.insert("app")
print(trie.search("app"))  # returns true