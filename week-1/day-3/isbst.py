class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
prev=None
def isbst(root):
    global prev
    prev=None
    return isbst_rec(root)
def isbst_rec(root):
    global prev 
    if root is None:
        return True
    if isbst_rec(root.left) is False:
        return False
    if prev is not None and prev.data>root.data:
        return False
    prev=root
    return isbst_rec(root.right)
root=Node(4)
root.left=Node(2)
root.right=Node(5)
root.left.left=Node(1)
root.left.right=Node(3)
root.right.left=Node(6)
if isbst(root):
    print("BST")
else:
    print("not a BST")
 