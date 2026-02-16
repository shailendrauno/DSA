class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
        if (root == None):
            return Node(value)
        if(root.data == value):
            return root
        if(root.data > value):
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
        return root

def search(root, value):
     if(root == None):
          print("Element not found", end="\n")
          return
     if(root.data == value):
          print("element is found", end="\n")
          return
     if(root.data > value):
           search(root.left, value)
     else:
           search(root.right, value)

def inOrder(root):
     if(root != None):
          inOrder(root.left)
          print(root.data, end= " ")
          inOrder(root.right)

root = insert(None, 1)
root = insert(root, 17)
root = insert(root, 47)
root = insert(root, 37)
root = insert(root, 14)
root = insert(root, 43)
root = insert(root, 84)
inOrder(root)
search(root,47)
search(root,100)










