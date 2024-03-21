from circular_queue import *

class CircularDeque(ArrayQueue): # 원형 큐 상속 받음
    def __init__(self, capacity = 10):
        super().__init__(capacity)

    # 동작이 원형 큐와 비슷한 연산
    def addRear(self, item): self.enqueue(item)
    def deleteFront(self): return self.dequeue()
    def getFront(self): return self.peek()

    # 원형 덱에 추가된 연산
    def addFront(self, item):
        if not self.isFull():
            self.array[self.front] = item
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else: pass
    def deleteRear(self):
        if not self.isEmpty():
            item = self.array[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity
            return item
        else: pass
    def getRear(self):
        if not self.isEmpty():
            return self.array[self.rear]
        else: pass

if __name__ == "__main__":
    dq = CircularDeque()

    for i in range(9):
        if i % 2 == 0 : dq.addRear(i)
        else: dq.addFront(i)
    dq.display("홀수는 전단 삽입, 짝수는 후단 삽입")

    for i in range(2): dq.deleteFront()
    for i in range(3): dq.deleteRear()
    dq.display("전단 삭제 2번, 후단 삭제 3번")

    for i in range(9, 14): dq.addFront(i)
    dq.display("전단에 9 ~ 13 삽입")
