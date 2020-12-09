class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s2) == len(s1) and s2 in (s1 + s1)
