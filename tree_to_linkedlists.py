from node import Node

def createLinkedLists(node,array):
    addAtDepth(node,0,array)

def addAtDepth(node,level,array_of_lists):
    if node != None:
        head = Node(node.key)
        if len(array_of_lists) > level:
            head.next = array_of_lists[level]
            array_of_lists[level] = head
        else:
            array_of_lists.append(head)
        addAtDepth(node.leftChild,level+1,array_of_lists)
        addAtDepth(node.rightChild,level+1,array_of_lists)