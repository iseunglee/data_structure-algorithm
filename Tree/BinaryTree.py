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

    def postorder(n):
        if n is not None:
            postorder(n.left)
            postorder(n.right)
            print(n.data, end=' ')