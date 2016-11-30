class Solution(object):
    def listToNum(self,head):
        string, cur = "", head
        while cur:
            string += str(cur.val)
            cur = cur.next
        return int(string)
    def numToList(self,val):
        string = str(val)
        head = ListNode(string[0]) 
        cur = head
        for i in xrange(1,len(string)):
            char = string[i]
            nxt = ListNode(int(char))
            cur.next = nxt
            cur = nxt
        return head
            
            
            
    def plusOne(self, head):
        val = self.listToNum(head)
        return self.numToList(val+1)