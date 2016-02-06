from binarysearchtree import TreeNode

def array_to_BST(array,tree):
    return addMiddle(tree,array,0,len(array)-1)
    
def addMiddle(tree,array,p,r):
    if p<=r:
        q = (p+r)//2
        tree.add(array[q],0)
        addMiddle(tree,array,p,q-1)
        addMiddle(tree,array,q+1,r)

def main(array):
    return attachChildren(array,0,len(array)-1)

def attachChildren(array,p,r):
    if p>r:
        return None
    else:
        q = (p+r)//2
        root = TreeNode(array[q],0)
        root.leftChild = attachChildren(array,p,q-1)
        root.rightChild = attachChildren(array,q+1,r)
        return root