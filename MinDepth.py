'''
Find the minimum depth to a leaf node
'''
class Solution(object):
    def minDepthHelper(self, root, height):
        if not root:
            return height
        if root.left and not root.right:
          return self.minDepthHelper(root.left, height + 1)
        elif root.right and not root.left:
          return self.minDepthHelper(root.right, height + 1)
        else:
            return min(self.minDepthHelper(root.left,height+1), self.minDepthHelper(root.right, height+1))
    
    def minDepth(self, root):
        return self.minDepthHelper(root, 0)