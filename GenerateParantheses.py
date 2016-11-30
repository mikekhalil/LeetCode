class Solution(object):
    def generateParenthesis(self, n):
        prev = ['()']
        for i in xrange(1,n):
            prev = self.generateStrings(prev, i)
        
        return prev
        
    def generateStrings(self, prevResult, n):
        uniqueSolutions = set()
        for str in prevResult:
            for i in xrange(len(str)):
                newString = str[0:i] + '()' + str[i:]
                print newString
                uniqueSolutions.add(newString)
        
        return list(uniqueSolutions)