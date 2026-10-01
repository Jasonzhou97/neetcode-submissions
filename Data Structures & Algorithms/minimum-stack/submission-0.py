class MinStack:

    def __init__(self):
        self.items = []

    def push(self, val: int) -> None:
        self.items.insert(0,val)

    def pop(self) -> None:
        item = self.items.pop(0)
        return item

    def top(self) -> int:
        return self.items[0]

    def getMin(self) -> int:
        return min(self.items)
