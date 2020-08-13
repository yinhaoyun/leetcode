class CombinationIterator:

    def __init__(self, s: str, combination_len: int):
        self.s = s
        self.len = combination_len
        self.combos = [i for i in range(2**len(s) - 1, -1, -1) if bin(i).count('1') == self.len]
        # print([bin(c) for c in self.combos])
        self.index = 0

    def next(self) -> str:
        bits = bin(self.combos[self.index])[2:]
        bits = ("0" * (len(self.s) - len(bits))) + bits
        # print(bits)
        self.index += 1
        return ''.join([self.s[i] for i, b in enumerate(bits) if b == '1'])

    def hasNext(self) -> bool:
        return self.index < len(self.combos)

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    obj = CombinationIterator('abc', 2)
    print(obj.next()) # ab
    print(obj.hasNext()) # True
    print(obj.next()) # ac
    print(obj.hasNext()) # True
    print(obj.next()) # bc
    print(obj.hasNext()) # False
