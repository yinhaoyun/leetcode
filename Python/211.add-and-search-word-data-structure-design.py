class WordDictionary:
    def __init__(self):
        self.children = dict()
        self.is_end = False

    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            cur = cur.children.setdefault(c, WordDictionary())
        cur.is_end = True

    def search(self, word: str) -> bool:
        # print("search: ", word)
        if len(word) == 0:
            return self.is_end
        if word[0] == ".":
            for trie in self.children.values():
                if trie.search(word[1:]):
                    return True
        elif word[0] in self.children:
            return self.children[word[0]].search(word[1:])
        return False


w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
print(w.search("pad"))  # False
print(w.search("bad"))  # True
print(w.search(".ad"))  # True
print(w.search("b.."))  # True
