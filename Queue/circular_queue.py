class ArrayQueue:
    def __init__(self, capacity = 10): # 생성자 정의
        self.capacity = capacity # 용량(고정)
        self.array = [None] * capacity # 요소들을 저장할 배열
        self.front = 0 # 전단 인덱스
        self.rear = 0 # 후단 인덱스

    def isEmpty(self): # 공백 상태
        return self.front == self.rear
    
    def isFull(self): # 포화 상태
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, item): # 삽입 연산
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else: pass # 오버플로우 에러
    
    def dequeue(self): # 삭제 연산
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: pass # 언더플로우 에러

    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else: pass
    
    def size(self):
        return (self.rear - self.front + self.capacity) % self.capacity
    
    def display(self, msg): # 전체 요소를 출력, msg : 큐의 이름이나 메시지를 출력하기 위한 매개변수
        print(msg, end = "= [")
        for i in range(self.front + 1, self.front + 1 + self.size()):
            print(self.array[i % self.capacity], end = " ")
        print("]")
    
    # 링 버퍼 구현을 위한 수정된 enqueue 연산
    def enqueue2(self, item):
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item # 일단 무조건 삽입
        if self.isEmpty(): # front == rear
            self.front = (self.front + 1) % self.capacity # 삽입 후 front 회전 -> 가장 오래된 요소 삭제

# 원형 큐 테스트
if __name__ == "__main__":
    import random
    q = ArrayQueue(8)

    q.display("초기상태")
    while not q.isFull():
        q.enqueue(random.randint(0, 100))
    q.display("포화 상태")

    print("삭제 순서: ", end = "")
    while not q.isEmpty():
        print(q.dequeue(), end = " ")
    print()

# 링 버퍼 테스트
if __name__ == "__main__":
    q = ArrayQueue(8)

    q.display("초기상태")
    for i in range(6):
        q.enqueue2(i)
    q.display("삽입 0-5")

    q.enqueue2(6); q.enqueue2(7)
    q.display("삽입 6, 7")

    q.enqueue2(8); q.enqueue2(9)
    q.display("삽입 8, 9")

    q.dequeue(); q.dequeue()
    q.display("삭제 x2")
