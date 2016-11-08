class Solution:
    def reverseWords(self, s):
        sentence = s.split()[::-1]
        reversedString = ""
        for word in sentence:
            reversedString += word + " "
        
        if len(reversedString) > 0:
            reversedString = reversedString[:-1]
            print reversedString
        

        return reversedString
    
if __name__ == "__main__":
    sol = Solution()
    s = sol.reverseWords("i like potatoes")
    print s 
