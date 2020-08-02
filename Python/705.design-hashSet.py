class MyHashSet:
    DATA_SIZE = 100
    AN_ODD_NUMBER = 32345
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = [[] for _ in range(MyHashSet.DATA_SIZE)]

    @staticmethod
    def hash_func(key: int) -> int:
        return (key * MyHashSet.AN_ODD_NUMBER) % MyHashSet.DATA_SIZE

    def add(self, key: int) -> None:
        i = MyHashSet.hash_func(key)
        if key not in self.data[i]:
            self.data[i].append(key)

    def remove(self, key: int) -> None:
        i = MyHashSet.hash_func(key)
        if key in self.data[i]:
            self.data[i].remove(key)

    def contains(self, key: int) -> bool:
        i = MyHashSet.hash_func(key)
        return key in self.data[i]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
hashSet = MyHashSet();
hashSet.add(1);
hashSet.add(2);
print(hashSet.contains(1))  # True
print(hashSet.contains(3))  # False
hashSet.add(2);
print(hashSet.contains(2))  # True
hashSet.remove(2);
print(hashSet.contains(2))  # False