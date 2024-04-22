class DNode:
    def __init__(self, elem, next=None, prev=None):
        self.data = elem # 노드의 데이터 필드(요소)
        self.next = next # 다음 노드를 위한 링크
        self.prev = prev # 이전 노드를 위한 링크

    # self 다음에 node를 넣는 append() 연산
    def append(self, node):
        if node is not None:
            node.next = self.next # 추가되는 노드의 다음 노드를 설정
            node.prev = self # 추가되는 노드의 이전 노드를 설정
            if node.next is not None: # self의 다음노드가 None이 아니면
                node.next.prev = node # 그 노드의 이전 노드는 node
                self.next = node # 첫 번째 노드의 다음 노드는 node
                