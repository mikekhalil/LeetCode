class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
            
        max_len = 0
        start, charsToIndex = 0, {}
        for i, char in enumerate(s):
            if charsToIndex.get(char,-1) >= charsToIndex.get(s[start]):
                start = charsToIndex.get(char,-1) + 1
                
            charsToIndex[char] = i
            max_len = max(max_len, i - start + 1)
        return max_len