class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
            
        prefix = strs[0]
        for i in xrange(1,len(strs)):
            s = strs[i]
            count = 0
            j = 0
            while j < len(prefix) and j < len(s) and prefix[j] == s[j]:
                count += 1
                j += 1
                
            if len(prefix) > count:
                prefix = prefix[0:count]
            
        
        return prefix