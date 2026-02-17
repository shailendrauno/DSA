class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

def insert(root, value):
    if(root == None):
        return Node(value)
    if(root.data == value):
        return root
    if(root.data > value):
        root.left = insert(root.left, value)
    else:
       root.right = insert(root.right, value)
    return root

def inOreder(root):
    if(root != None):
        inOreder(root.left)
        print(root.data, end= " ",)
        inOreder(root.right)

def search(root, value):
    if(root == None):
        print("the element is not find in the tree", end="\n")
        return
    if(root.data == value):
        print("the element is find in the tree", end="\n")
        return
    if(root.data > value):
        search(root.left, value)
    else:
        search(root.right, value)

def get_succsesor(root):
    root = root.right
    while(root != None and root.left != None):
        root = root.left
    return root

def delete(root, value):
    if(root == None):
        return root
    if(root.data > value):
        root.left = delete(root.left, value)
    elif(root.data < value):
        root.right = delete(root.right, value)
    else:
        if(root.left == None):
            return root.right
        if(root.right == None):
            return root.left
        else:
            succ = get_succsesor(root)
            root.data = succ.data
            root.right = delete(root.right, succ.data)
        
    return root
    

root = insert(None, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 4)
root = insert(root, 10)
root = insert(root, 13)
root = insert(root, 14)
inOreder(root)
search(root,12)
search(root,32)
delete(root, 3)
inOreder(root)
root = insert(None, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 4)
root = insert(root, 10)
root = insert(root, 13)
root = insert(root, 14)
inOreder(root)
search(root,12)
search(root,32)
delete(root, 3)
inOreder(root)