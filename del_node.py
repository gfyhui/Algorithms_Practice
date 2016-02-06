def delNode(node):
    #Assume length of linked list is odd
    current = node
    while current.next.next != None:
        current.data = current.next.data
        current = current.next
    current.next = None