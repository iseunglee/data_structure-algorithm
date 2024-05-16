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
                
    # self 다음 노드 삭제 연산
    def popNext(self):
        node = self.next # 삭제할 노드
        if node is not None:
            self.next = node.next # 현재 노드의 다음노드는 원래 있던 node의 다음 
            self.next.prev = self # 다음 노드 (self.next)의 이전 노드는 self


class DbLinkedList: # 이중 연결 리스트 클래스
    def __init__(self): # 생성자
        self.head = None # head 선언 및 None으로 초기화

    # 포화 상태 공백 상태 검사
    def isEmpty(self):
        return self.head == None # 만약 공백이라면 head가 None일 것이고, 그렇다면 True를 반환할 것이다.
    def isFull(self):
        return False # 연결된 구조는 메모리만 있다면 무한정 노드를 추가할 수 있으므로 포화 상태일 수 없다. 따라서 False를 반환한다.
    
    # pos번째 요소를 찾기 위해 먼저 pos번째 노드를 찾는다.
    def getNode(self, pos):
        if pos < 0: return None # 잘못된 위치 None 반환
        
        ptr = self.head # 시작 위치 -> head
        
        for i in range(pos): # pos 위치까지 pos번 반복, 머리 노드에서부터 링크를 따라 pos번 이동하면 pos위치의 노드에 도착
            if ptr == None:
                return None
            ptr = ptr.next
        return ptr

    # pos번째 노드의 데이터를 위에서 정의한 getNode() 메소드를 이용한다
    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구하고
        if node == None: return None # 해당 노드가 없는 경우
        else: return node.data # 노드의 데이터를 추출

    # 전체 요소의 수를 구하는 연산
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None: # ptr이 None이면 진행 중지하고 count를 반환함
            ptr = ptr.next
            count += 1
        return count

    # 화면에 보기 좋게 출력하는 연산
    def display(self, msg='DbLinkedList: '):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end="<=>") # 이중 연결은 <=>로 표시
            ptr = ptr.next
        print('None')

    # pos위치에 새로운 요소를 삽입하는 insert(pos, e) 연산
    def insert(self, pos, e):
        node = DNode(e) # 삽입할 이중 연결 구조의 노드 생성
        before = self.getNode(pos-1) # 삽입할 위치 이전의 노드 탐색

        if before == None: # 삽입 위치가 머리 노드라면
            node.next = self.head # 삽입하는 node의 다음 노드를 삽입 전 머리 노드로 지정
            if node.next is not None: # node.next(self.head)가 None이 아니라면
                node.next.prev = node # 전 노드는 삽입한 node가 됨
            self.head = node # 머리노드를 삽입한 node로 설정
        
        else: before.append(node) # 머리노드가 아닌 경우 before 다음에 추가

    # pos 위치의 요소를 삭제하는 delete(pos) 연산
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None: # 머리 노드 삭제인 경우
            before = self.head # 삭제 후 출력하기 위해 before에 현재 머리노드 담기
            
            if self.head is not None: # 현재 머리노드가 None이 아니라면
                self.head = self.head.next # 새로운 머리노드는 현재 머리노드의 다음노드가 됨
            if self.head is not None: # 새로운 머리노드가 None이 아니라면
                self.head.prev = None # 머리노드는 이전 노드가 None이 되므로 
            return before # 삭제되는 노드 출력
        
        else: before.popNext() # 머리노드 삭제가 아닌 경우, before의 다음 노드 삭제

