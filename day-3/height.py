class Height:
	def __init__(self):
		self.height=0
class Node:
	def __init__(self,data):
		self.data=data
		self.right=None
		self.left=None
def isBalanced(root,height):
	left_height=Height()
	right_height=Height()
	if root is None:
		return True
	lef=isBalanced(root.left,left_height)
	rig=isBalanced(root.right,right_height)
	height.height=max(left_height.height,right_height.height)+1
	if abs(left_height.height-right_height.height)<=1:
		return lef and rig
	return False
height=Height()
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)
root.right.left=Node(7)
root.left.left.left=Node(8)
root.left.left.left.left=Node(9)
if isBalanced(root,height):
	print("balanced")
else:
	print("not balanced")


