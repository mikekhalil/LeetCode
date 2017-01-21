class Solution(object):
    def getCount(self, s):
        char_map = {}
        for char in s:
            if char in char_map:
                char_map[char] += 1
            else:
                char_map[char] = 1
        return char_map
    
	def numOdd(self,char_map):
        numOdd = 0
        for key,val in char_map.iteritems():
            if val % 2 != 0:
                numOdd += 1
        return numOdd
            
    def canPermutePalindrome(self, s):
        even = len(s) % 2 == 0
        char_map = self.getCount(s)
        num_odd = self.numOdd(char_map)
        return (even and num_odd == 0) or (not even and num_odd == 1)