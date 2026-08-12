import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub('[^0-9a-zA-Z]+', '', s).strip().lower()
        p1 = 0
        p2 = len(s2) - 1
    
        while p2 > p1:
            if s2[p1] != s2[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True
    
    