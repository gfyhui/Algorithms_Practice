def partition(node,x):
    lessInitialized = False
    greaterInitialized = False
    less = None
    greater_head = None
    greater_tail = None
    greater_head_init = False
    current = node
    while current != None:
        if current.data < x:
            if lessInitialized:
                less.next = current
                less = less.next
            else:
                less = current
                lessInitialized = True
        else:
            if greaterInitialized:
                greater_tail.next = current
                greater_tail = greater_tail.next
                if not greater_head_init:
                    greater_head.next = greater_tail
                    greater_head_init = True
            else:
                greater_head = current
                greater_tail = current
                greaterInitialized = True
        current = current.next
    greater_tail.next = None
    less.next = greater_head