from node import Node

def deleteDuplicates(head):
    if head == None:
        return head
    current = head
    while current != None:
        temp = current.next
        hasDuplicates = False
        while temp and temp.data == current.data:
            temp = temp.next
            hasDuplicates = True
        if hasDuplicates:
            if temp:
                current.data = temp.data
                current.next = temp.next
            else:
                current.next = None
                if head.next == None:
                    head = None
                else:
                    runner = head
                    while runner.next != current:
                        runner = runner.next
                    runner.next = current.next
        else:
            current = current.next
    return head

a = Node(1)
a.append(2)
a.append(3)
a.append(2)
a.append(1)
print a
b = deleteDuplicates(a)
print b
    # return head