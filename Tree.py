
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def preOrder(root):
    if (root != None):
        print(root.data, end=" ")
        preOrder(root.left)
        preOrder(root.right)

def inOrder(root):
    if(root != None):
        inOrder(root.left)
        print(root.data, end= " ")
        inOrder(root.right)

def postOrder(root):
    if(root != None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end= " ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)
preOrder(root)
inOrder(root)
postOrder(root)