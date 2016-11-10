class Solution():
    def findPathSum(self,root,val, target):
        val += root.val
        
        if not root.left and not root.right:
            #leaf node
            return val
        
        if root.left:
            leftPath = self.findPathSum(root.left, val, target)
            if leftPath == target:
                return target
        if root.right:
            rightPath = self.findPathSum(root.right, val, target)
            if rightPath == target:
                return target
        
    
    def hasPathSum(self, root, target):
        if root == None:
            return False
        return self.findPathSum(root,0,target) == target