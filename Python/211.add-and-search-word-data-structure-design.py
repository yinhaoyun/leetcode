import collections


class WordDictionary:
    def __init__(self):
        self.children = collections.defaultdict(WordDictionary)

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.children[""] = WordDictionary()
            return
        self.children[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.children.get("") is not None
        if word[0] == ".":
            for key, trie in self.children.items():
                if trie.search(word[1:]):
                    return True
        elif not self.children.get(word[0]):
            return False
        return self.children[word[0]].search(word[1:])


w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
print(w.search("pad"))
print(w.search("bad"))
print(w.search(".ad"))
print(w.search("b.."))
