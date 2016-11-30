class Solution(object):
    def reverseList(self, head):
        if head == None or head.next == None:
            return head
        
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rev