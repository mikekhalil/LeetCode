#sorted list
class Solution(object):
    def deleteDuplicates(self, head):
        if head == None:
            return head
        prev = head
        cur = head.next
        while cur != None:
            if prev.val == cur.val:
                prev.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                prev = prev.next
        return head