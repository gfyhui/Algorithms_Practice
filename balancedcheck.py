

def height(node):
    if node == None:
        return 0
    else:
        return 1 + max(height(node.left),height(node.right))
        
def isBalanced(node):
    if node == None:
        return True
    elif abs(height(node.left) - height(node.right)) > 1:
        return False
    else:
        return isBalanced(node.left) and isBalanced(node.right)
