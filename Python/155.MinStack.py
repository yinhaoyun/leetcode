import heapq


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            self.stack.append((val, min(val, self.stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

class MinStack_heap:

    def __init__(self):
        self.stack = []
        self.pq = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.pq, val)

    def pop(self) -> None:
        val = self.stack.pop()
        self.pq.remove(val)
        heapq.heapify(self.pq)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.pq[0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()