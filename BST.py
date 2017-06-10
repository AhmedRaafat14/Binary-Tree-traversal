import Queue


class Node:
    def __init__(self, data):
        self.nodeData = data
        self.leftNode = None
        self.rightNode = None


def display(root, full_depth):
    if root == None:
        return
    if full_depth == 0:
        print root.nodeData,

    display(root.leftNode, full_depth - 1)
    display(root.rightNode, full_depth - 1)

def display1(root):
    if root == None:
        return

    nodes = Queue.Queue()

    nodes.put(root)

    while 1:

        if nodes.qsize() == 0:
            break
        nodeLevels = nodes.qsize()
        while nodeLevels > 0:
            node = nodes.get()

            print node.nodeData,

            if node.leftNode != None:
                nodes.put(node.leftNode)
            if node.rightNode != None:
                nodes.put(node.rightNode)
            nodeLevels -= 1

        print("")




'''
    Binary Tree used:
                
                    1
                /        \
               4          5
             /    \       /  \
            2      8      3   7
           /  \    /\         / \ 
           0   1  3  9        1  10
'''

root = Node(1)
root.leftNode  = Node(4)
root.rightNode = Node(5)

root.leftNode.leftNode  = Node(2)    # left child for node 4
root.leftNode.rightNode = Node(8)   # right child for node 4

root.rightNode.leftNode  = Node(3)   # left child for node 5
root.rightNode.rightNode = Node(7)  # right child for node 5

root.leftNode.leftNode.leftNode  = Node(0)   # left child for node 2
root.leftNode.leftNode.rightNode = Node(1)  # right child for node 2

root.leftNode.rightNode.leftNode  = Node(3)   # left child for node 8
root.leftNode.rightNode.rightNode = Node(9)  # right child for node 8

root.rightNode.rightNode.leftNode  =  Node(1)  # Left child for node 7
root.rightNode.rightNode.rightNode =  Node(10) # right child for node 7


# for i in range(0, 4):
#     display(root, i)
#     print("")

display1(root)
