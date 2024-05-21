from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, elem):
        self.q1.put(elem)

    def pop(self):
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return self.q2.get()