# DIAMETER ( WIDTH ) OF A BINARY TREE WITH O(N) COMPLEXITY

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

class Height:
    def __init__(self):
        self.h = 0

def diameter(root,height):
    lh = Height()
    rh = Height()
    if(root == None):
        height.h = 0
        return(0)
    ldiameter = diameter(root.left,lh)
    rdiameter = diameter(root.right,rh)
    height.h = max(lh.h,rh.h) + 1
    return(max(lh.h + rh.h + 1,max(ldiameter,rdiameter)))

def printdia(root):
    height = Height()
    return(diameter(root,height))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
