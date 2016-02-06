def kthelement(k,node):
    current = node
    length = 0
    while current != None:
        length = length + 1
        current = current.next
    
    if k > length:
        raise ValueError('k is greater than length of linked list')
    elif k < 1:
        raise ValueError('k must be greater than 0')
    current = node
    for i in range(length-k):
        current = current.next
    return current.data