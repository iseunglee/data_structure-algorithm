from circular_queue import ArrayQueue

# 원형 큐를 활용한 피보나치 수열 구현
q = ArrayQueue() # 원형 큐 객체 생성
q.enqueue(0) # 0 삽입
q.enqueue(1) # 1 삽입
print('F(0) = 0')
print('F(1) = 1')

for i in range(2, 20):
    val = q.dequeue() + q.peek()
    q.enqueue(val)
    print(f'F({i}) = ', val)