class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                elem = stack.pop()
                if ord(elem) + 2 != ord(char) and ord(elem) + 1 != ord(char):
                    return False
        if len(stack) != 0:
            return False
                
        return True
        