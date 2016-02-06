from node import Node

def list_to_number_normal(node):
    current = node
    list_array = []
    while current != None:
        list_array.append(current.data)
        current = current.next
    number = 0
    digit = 0
    for i in range(len(list_array)-1,-1,-1):
        number = number + (10**digit)*list_array[i]
        digit = digit + 1
    return number

def number_to_list_normal(number):
    head = Node(number%10)
    number = number//10
    while number > 0:
        temp = Node(number%10)
        temp.next = head
        head = temp
        number = number//10
    return head

def list_to_number(node):
    current = node
    list_array = []
    while current != None:
        list_array.append(current.data)
        current = current.next
    temp = list_array[0]
    list_array[0] = list_array[-1]
    list_array[-1] = temp
    number = 0
    digit = 0
    for i in range(len(list_array)-1,-1,-1):
        number = number + (10**digit)*list_array[i]
        digit = digit + 1
    return number
    
def number_to_list(number):
    head = Node(number%10)
    number = number//10
    if number == 0:
        return head
    previous = Node(number%10)
    tail = previous
    number = number //10
    while number > 0:
        front = Node(number%10)
        front.next = previous
        previous = front
        number = number//10
    second = previous.next
    tail.next = previous
    previous.next = None
    head.next = second
    return head

def addLists_normal(nodeA, nodeB):
    if not (nodeA or nodeB):
        raise ValueError('nodes cannot be null')
    number = list_to_number_normal(nodeA) + list_to_number_normal(nodeB)
    return number_to_list_normal(number)

def addLists(nodeA, nodeB):
    if not (nodeA or nodeB):
        raise ValueError('nodes cannot be null')
    number = list_to_number(nodeA) + list_to_number(nodeB)
    return number_to_list(number)
    