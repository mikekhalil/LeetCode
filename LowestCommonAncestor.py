class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None:
            return None
        
        print root.val 
        smaller, larger = min(p.val,q.val), max(p.val, q.val)
        if smaller <= root.val and larger >= root.val:
            return root
        elif smaller >= root.val and larger >= root.val:
            return self.lowestCommonAncestor(root.right, p,q)
        else:
            return self.lowestCommonAncestor(root.left,p,q)