class Solution(object):
    def generatePossibleNextMoves(self, s):
        combos = []
        for i in xrange(1, len(s)):
            if s[i] == "+" and s[i-1] == "+":
                newCombo = s[:i-1] + "--" + s[i+1:]
                combos.append(newCombo)
        return combos