class Solution(object):
    def flatten(self, root):
        if not root:
            return 
        
        if root.left and not root.right:
            self.flatten(root.left)
            root.right = root.left
            root.left = None
            
        elif root.right and not root.left:
            self.flatten(root.right)
            
        elif root.right and root.left:
            self.flatten(root.left)
            self.flatten(root.right)
            right = root.right
            root.right = root.left
            cur = root.left
            while cur.right:
                cur = cur.right
            cur.right = right
            root.left = None