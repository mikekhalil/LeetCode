# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#this solution is based off of top solution on leet code in Java
class Solution(object):
	def isSymmetric(root):
		if root == None:
			return True
		return self.isSymmetricHelper(root.left,root.right)
	
	def isSymmetricHelper(p , q):
		if not p and not q: 
			return True
		if not p or not q: 
			return False
		return p.val == q.val and self.isSymmetricHelper(p.left, q.right) and self.isSymmetricHelper(p.right,q.left)

    
		
        