from data_structure.trie import Trie


class WordDictionary:
    def __init__(self):
        self.tries = dict()

    def addWord(self, word: str) -> None:
        n = len(word)
        self.tries.setdefault(len(word), Trie()).addWord(word)

    def search(self, word: str) -> bool:
        n = len(word)
        if self.tries.get(n) is None:
            return False
        return self.tries[n].search(word)


w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
print(w.search("pad"))  # False
print(w.search("bad"))  # True
print(w.search(".ad"))  # True
print(w.search("b.."))  # True
