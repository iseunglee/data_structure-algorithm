from circular_queue import ArrayQueue

class BTNode:
    def __init__(self, elem, left=None, right=None):
        self.data = elem
        self.left = left
        self.right = right

def preorder(n): # 이진트리의 전위순회
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

def inorder(n): # 이진트리의 중위순회
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

def postorder(n): # 이진트리의 후위순회
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

def levelorder(root): # 이진 트리의 레벨 순회
    queue = ArrayQueue() # 큐 객체 초기화
    queue.enqueue(root) # 루트 노드 큐에 삽입
    while not queue.isEmpty(): # 큐가 공백 상태가 아닌 동안,
        n = queue.dequeue() # 큐에서 하나의 노드를 꺼내고
        if n is not None: # 이 노드가 None이 아니면
            print(n.data, end=' ') # n의 데이터를 프린트
            queue.enqueue(n.left) # 큐에 왼쪽 자식을 삽입
            queue.enqueue(n.right) # 큐에 오른쪽 자식을 삽입

def count_node(n): # 이진트리의 노드 개수 구하기
    if n is None:
        return 0
    else:
        return count_node(n.left) + count_node(n.right) + 1
    
def calc_height(n): # 이진트리의 높이 구하기
    if n is None:
        return 0
    
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)

    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1

# 코드 4.8: 이진트리 연산들의 테스트 프로그램
if __name__ == "__main__":
    d = BTNode('D', None, None)
    e = BTNode('E', None, None)
    b = BTNode('B', d, e)
    f = BTNode('F', None, None)
    c = BTNode('C', f, None)
    root = BTNode('A', b, c)

    print('\n   In-Order : ', end=''); inorder(root)
    print('\n  Pre-Order : ', end=''); preorder(root)
    print('\n Post-Order : ', end=''); postorder(root)
    print('\nLevel-Order : ', end=''); levelorder(root)
    print()

    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 트리의 높이 = %d" % calc_height(root))