class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.current = 0

    def append(self, item):
        if len(self.storage) == self.capacity:
            self.storage[self.current] = item
            self.current = (self.current+1) % self.capacity
        else:
            self.storage.append(item)

    def get(self):
        return self.storage
