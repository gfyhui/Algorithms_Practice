from node import Node

def noDuplicates(node):
    elements = set()
    if node == None:
        raise ValueError('Empty node')
    else:
        current = node
        elements.add(current.data)
        while current != None and current.next != None:
            print elements
            if current.next.data in elements:
                current.next = current.next.next
            else:
                elements.add(current.next.data)
                current = current.next
            if current == None:
                break

def noBuffer(node):
    if node == None:
        raise ValueError('Node is null')
    current = node
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next