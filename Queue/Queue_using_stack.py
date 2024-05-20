class Queue():
    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, elem):
        self.instack.append(elem)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()