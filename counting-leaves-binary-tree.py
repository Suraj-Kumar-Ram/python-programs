# COUNTING LEAVES OF A BINARY TREE

class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None

def count_leaves(node):
    if(node == None):
        return(0)
    if(node.left == None or node.right == None):
        return(1)
    else:
        return(count_leaves(node.left) + count_leaves(node.right))

node = Node(1)
node.left = Node(2)
node.right = Node(3)
node.left.left = Node(4)
node.left.right = Node(5)
k = count_leaves(node)