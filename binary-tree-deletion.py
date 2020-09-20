# PROGRAM TO DELETE A GIVEN BINARY TREE

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        
def postorder_delete(root,c):
    if(root!=None):
        postorder_delete(root.left,c)
        postorder_delete(root.right,c)
        root.data = None
        c.append(root.data)
    return(c)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)