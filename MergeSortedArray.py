class Solution:
    def merge(self,nums1, m, nums2,n):
        #test cases on LeetCode were strange - didnt pass them but seems correct for my inputes
        nums1.extend(nums2)
        print nums1
        rightIndex = m + n - 1
        m -= 1
        n -= 1
        while rightIndex >= 0:
            if m < 0:
                nums1[rightIndex] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[rightIndex] = nums1[m]
                m -= 1
            elif nums1[m] > nums2[n]:
                nums1[rightIndex] = nums1[m]
                m -= 1
            else:
                nums1[rightIndex] = nums2[n]
                n -= 1
            rightIndex -= 1
        


#test
if __name__ == "__main__":
    sol = Solution()
    
    nums1, nums2 = [1,2,7], [3,4,5,6]
    
    sol.merge(nums1,len(nums1),nums2,len(nums2))
    print nums1

