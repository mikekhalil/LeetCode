class Solution(object):
    def isValid(self, s):
        brackets = { '(' : ')' , '{' : '}', '[' : ']' }
        stack = []
        for char in s:
            char =  str(char)
            if char in brackets.keys():
                stack.append(char)
                
            else:
                if len(stack) == 0:
                    return False
                else:
                    last = stack.pop()
                    if brackets[last] != char:
                        return False
        if len(stack) == 0:
            return True
        return False