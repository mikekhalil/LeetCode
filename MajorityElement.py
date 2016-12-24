'''
Find majority element in array
'''
class Solution(object):
    def majorityElement(self, nums):
        value = nums[0]
        count = 1
        for num in nums:
            if value == num:
                count += 1
            else:
                count -= 1
            
            if count == 0:
                value = num
                count = 1
        return value


if __name__ == "__main__":
    sol = Solution()
    print sol.majorityElement([1,1,2,2,2])

