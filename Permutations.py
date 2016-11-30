class Solution(object):
    def permute(self, nums):
        if len(nums) == 1 or len(nums) == 0:
            return [nums]
            
        allPermutations = [] #list of lists
        for i in xrange(len(nums)):
            #get all permuations for a list start with a specific number
            subList = self.permute(nums[:i]+nums[i+1:])
            for item in subList:
                item.append(nums[i])
            allPermutations.extend(subList)
            print subList
        
        return allPermutations