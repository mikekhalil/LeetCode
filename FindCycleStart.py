"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
"""
class Solution(object):
    def detectCycle(self, head):
        if not head: 
            return None
        
        walker =  runner = head
        found = False
        while runner and runner.next:
            if not found:
                walker = walker.next
                runner = runner.next.next
                if walker == runner:
                    #reset walker to head and then move each pointer by 1 increment
                    walker = head
                    found = True
            else:
                #once walker and runner intersect again, we know this is the start of the cycle
                if walker == runner:
                    return walker
                walker = walker.next
                runner = runner.next
               
        
        return None