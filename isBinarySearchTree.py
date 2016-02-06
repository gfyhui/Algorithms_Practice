def isBST(node):
    if node == None:
        return True
    else:
        if check(node):
            return isBST(node.leftChild) and isBST(node.rightChild)
        else:
            return False

def check(node):
    left = node.leftChild
    right = node.rightChild
    if left != None and left.key > node.key:
        return False
    if right != None and right.key <= node.key:
        return False
    return True