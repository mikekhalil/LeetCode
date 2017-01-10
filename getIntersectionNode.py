class Solution(object):
    def listLength(self,root):
        cur, length = root, 0
        while cur:
            cur = cur.next
            length += 1
        return length
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        dif = self.listLength(headA) - self.listLength(headB)
        if dif > 0:
            while dif != 0:
                headA = headA.next
                dif -= 1
        elif dif < 0:
            while dif != 0:
                headB = headB.next
                dif += 1
        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next