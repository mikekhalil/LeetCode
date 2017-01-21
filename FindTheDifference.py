class Solution(object):
    def getCharCount(self, string):
        char_count = {}
        for char in string:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        return char_count
        
    def findTheDifference(self, s, t):
        s_count, t_count = self.getCharCount(s), self.getCharCount(t)
        for key, val in t_count.iteritems():
            if key not in s_count:
                return key
            elif s_count[key] != val:
                return key