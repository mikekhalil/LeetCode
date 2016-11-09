class Solution(object):
    def isCloserToTarget(self, value,closest,target):
        return abs(value - target) < abs(closest - target)
        
    def search(self,root,target,closest):
        if root == None:
            return closest
        
        if closest == None or self.isCloserToTarget(root.val,closest,target):
            closest = root.val
        
        #get closest values in left and right sub trees
        leftSubTree = self.search(root.left,target,closest)
        rightSubTree = self.search(root.right,target,closest)
        
        #update closest value
        if self.isCloserToTarget(leftSubTree,closest,target):
            closest = leftSubTree
        
        if self.isCloserToTarget(rightSubTree,closest,target):
            closest = rightSubTree
    
        return closest
        
    def closestValue(self, root, target):
        return self.search(root, target, None)
