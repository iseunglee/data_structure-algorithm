from BinaryTree import BTNode

# 모스코드 표를 리스트로 변환
table =[('A', '.-'),    ('B', '-...'),  ('C', '-.-.'),  ('D', '-..'),
        ('E', '.'),     ('F', '..-.'),  ('G', '--.'),   ('H', '....'),
        ('I', '..'),    ('J', '.---'),  ('K', '-.-'),   ('L', '.-..'),
        ('M', '--'),    ('N', '-.'),    ('O', '---'),   ('P', '.--.'),
        ('Q', '--.-'),  ('R', '.-.'),   ('S', '...'),   ('T', '-'),
        ('U', '..-'),   ('V', '...-'),  ('W', '.--'),   ('X', '-..-'),
        ('Y', '-.--'),  ('Z', '--..') ]

def encode(ch):
    idx = ord(ch) - ord('A')
    return table[idx][1]

def decode_simple(morse):
    for tp in table:
        if morse == tp[1]:
            return tp[0]
        
def make_morse_tree(): # 모스코드 디코딩을 위한 결정 트리 만들기
    root = BTNode(None, None, None)
    for tp in table:
        code = tp[1]
        node = root # 루트부터 탐색
        for c in code:
            if c == '.':
                if node.left == None:
                    node.left = BTNode(None, None, None)
                node = node.left

            elif c == '-':
                if node.right == None:
                    node.right = BTNode(None, None, None)
                node = node.right
            
        node.data = tp[0] # 최종 노드에 문자 부여
    return root

def decode(root, code): # 루트 인자에 make_morse_tree()의 객체가 들어갈 수 있음 왜냐? 반환값이 만들어진 트리의 root값이기 때문에
    node = root
    for c in code:
        if c == '.':
            node = node.left
        elif c == '-':
            node = node.right

    return node.data

# 코드 4.14: 인코딩과 디코딩 테스트 프로그램
morseCodeTree = make_morse_tree()
str = input("입력 문장 : ")
mlist = []
for ch in str:
    code = encode(ch)
    mlist.append(code)
print("Morse Code: ", mlist)
print("Decoding  : ", end='')
for code in mlist:
    ch = decode(morseCodeTree, code)
    print(ch, end='')
print()