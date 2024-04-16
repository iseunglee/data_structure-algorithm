class Node: # 단순 연결 구조를 위한 노드 클래스
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

    def append(self, node): # self 다음에 node를 넣는 연산
        # 삽입할 노드가 None이 아니면
        if node is not None:
            node.link = self.link 
            self.link = node 
    
    def popNext(self): # self의 다음노들르 삭제하고 반환하는 연산
        next = self.link
        if next is not None:
            self.link = next.link
        return next
    
class LinkedList: # 단순 연결 구조를 위한 리스트 클래스
    def __init__(self):
        self.head = None # 시작 노드(머리 노드)를 가리키기 위한 헤드 선언, 맨 첨은 공백 상테이므로 None으로 초기화

    # 포화 상태 공백 상태 검사
    def isEmpty(self):
        return self.head == None # 만약 공백이라면 head가 None일 것이고, 그렇다면 True를 반환할 것이다.
    def isFull(self):
        return False # 연결된 구조는 메모리만 있다면 무한정 노드를 추가할 수 있으므로 포화 상태일 수 없다. 따라서 False를 반환한다.
    
    def getNode(self, pos):
        if pos < 0: return None # 잘못된 위치 None 반환
        
        ptr = self.head # 시작 위치 -> head
        
        for i in range(pos): # pos 위치까지 pos번 반복, 머리 노드에서부터 링크를 따라 pos번 이동하면 pos위치의 노드에 도착
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr
