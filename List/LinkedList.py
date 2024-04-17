class Node: # 단순 연결 구조를 위한 노드 클래스
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

    def append(self, node): # self 다음에 node를 넣는 연산
        # 삽입할 노드가 None이 아니면
        if node is not None:
            node.link = self.link 
            self.link = node 
    
    def popNext(self): # self의 다음노드를 삭제하고 반환하는 연산
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
    
    # pos번째 요소를 찾기 위해 먼저 pos번째 노드를 찾는다.
    def getNode(self, pos):
        if pos < 0: return None # 잘못된 위치 None 반환
        
        ptr = self.head # 시작 위치 -> head
        
        for i in range(pos): # pos 위치까지 pos번 반복, 머리 노드에서부터 링크를 따라 pos번 이동하면 pos위치의 노드에 도착
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr
    
    # pos번째 노드의 데이터를 위에서 정의한 getNode() 메소드를 이용한다
    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 구하고
        if node == None: return None # 해당 노드가 없는 경우
        else: return node.data # 노드의 데이터를 추출
    
    # pos번째 위치에 새로운 요소를 삽입하는 연산
    def insert(self, pos, e):
        node = Node(e, None) # 우선 위치가 없는 새로운 요소 e를 가지는 노드 생성
        before = self.getNode(pos-1) # pos 위치에 새로운 노드를 삽입하는 것은 pos-1이 수정되야하므로 이전 노드를 구해줌
        if before == None: # 이전 노드가 None이란 것은 새로 삽입할 위치가 제일 첫 노드라는 의미
            node.link = self.head # 머리 노드로 들어갈 node의 다음(node.link)은 삽입 전 머리 노드(self.head)를 설정하고
            self.head = node # 머리 노드를 뜻하는 변수(self.head)에 새롭게 들어갈 머리노드(node)를 설정
        else: before.append(node) # 머리 노드에 삽입하는 것이 아닌 경우

    # pos 위치의 요소를 삭제하는 연산
    def delete(self, pos):
        before = self.getNode(pos-1) # 삭제 연산 역시, 수정되는 부분의 삭제할 노드의 전 노드(before)
        if before == None: # 삭제할 노드의 전 노드(before)가 None이란 것은 삭제할 노드가 머리 노드라는 의미
            before = self.head # 전 노드(before)에 현재 머리노드 정보 넣고
            if self.head is not None: # 현재 리스트의 머리노드(self.head)가 None이 아니라면 
                self.head = self.head.link # 새로운 머리노드를 가리키는 포인터는 현재 head 포인터가 가리키는 노드의 다음 노드가 됨
            return before # 삭제할 요소 반환
        else: return before.popNext()

    # 전체 요소의 수를 구하는 연산
    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None: # ptr이 None이면 진행 중지하고 count를 반환함
            ptr = ptr.link
            count += 1
        return count

    # 화면에 보기 좋게 출력하는 연산
    def display(self, msg='LinkedList: '):
        print(msg, end='')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end="->")
            ptr = ptr.link
        print('None')
