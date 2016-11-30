from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        heapify(nums)
        numPops = len(nums) - k + 1
        val = None
        while numPops > 0:
            numPops -=1
            val = heappop(nums)
            
        return val