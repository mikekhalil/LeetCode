#naive solution - find a better one (TLE)
class Solution(object):
    def isPalindrome(self,string):
        return string == string[::-1]

    def longestPalindrome(self, string):
        #find the longest palindrome within a string
        i, j, pal = 0, 0, string[0]
        while i < len(string):
            j = i + 1
            while j < len(string):
                temp = string[i:j+1]
                if self.isPalindrome(temp) and len(temp) > len(pal):
                    pal = temp
                j += 1

            i += 1
        return pal


    


