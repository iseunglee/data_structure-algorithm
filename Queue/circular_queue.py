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

# 테스트
import random
q = ArrayQueue(8)

q.display("초기상태")