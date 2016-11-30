class Solution(object):
    def getChildren(self,root, children):
        if root == None:
            return True
        
        #populate children lists
        leftChildren, rightChildren = [], []
        left_validity = self.getChildren(root.left,leftChildren)
        right_validity = self.getChildren(root.right,rightChildren)
        
        if not left_validity or not right_validity:
            return False
        
        if len(leftChildren) > 0 and max(leftChildren) >= root.val:
            return False
        
        if len(rightChildren) > 0 and min(rightChildren) <= root.val:
            return False
        
        children.append(root.val)
        children.extend(leftChildren)
        children.extend(rightChildren)
        return True
        
        
        
    def isValidBST(self, root):
        return self.getChildren(root, [])