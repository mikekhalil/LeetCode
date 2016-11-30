class Solution(object):
    def strStr(self, haystack, needle):
        i = 0
        while i <= len(haystack) - len(needle):
            subString = haystack[i:i + len(needle)]
            print subString
            if subString == needle:
                return i
            i += 1
        return -1
        