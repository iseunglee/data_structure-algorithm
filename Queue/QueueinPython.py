# 파이썬 내장 큐 모듈을 사용하여 0~100까지의 랜덤 숫자를 삽입/삭제하는 코드
import queue
import random

q = queue.Queue(8) # 사이즈가 8인 큐 객체를 생성

print('삽입 순서: ', end = '')
while not q.full():
    v = random.randint(0, 100)
    q.put(v) # 삽입 put() 사용
    print(v, end = ' ')

print()

print('삭제 순서: ', end = '')
while not q.empty():
    print(q.get(), end = ' ') # 삭제 get() 사용

print()

