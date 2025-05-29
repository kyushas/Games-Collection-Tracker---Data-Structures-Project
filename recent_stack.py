class RecentGameStack:
    def __init__(self, capacity=10):
        self.stack = []
        self.capacity = capacity

    def push(self, game):
        if game in self.stack:
            self.stack.remove(game)  # remove existing to move it to top
        self.stack.append(game)
        if len(self.stack) > self.capacity:
            self.stack.pop(0)  # remove oldest

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None

    def get_recent(self):
        return self.stack[::-1]  # most recent first

    def is_empty(self):
        return len(self.stack) == 0
