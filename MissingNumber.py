class Solution(object):
    def missingNumber(self, nums):
        if len(nums) == 0:
            return None
        
        sums = sum_array = i = 0
        i = 1
        for num in nums:
            sum_array += num
            sums += i
            i += 1
            
        sums -= sum_array
        return sums