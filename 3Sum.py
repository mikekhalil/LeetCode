class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            target = -nums[i]
            tmp = {}
            for j in range(i+1, len(nums)):
                x = target - nums[j]
                if tmp.get(x) is None:
                    tmp[nums[j]] = j
                else:
                    if [nums[i],nums[j],nums[tmp[x]]] not in res:
                        res.append([nums[i],nums[j],nums[tmp[x]]])
        return res