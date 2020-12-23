from collections import defaultdict

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        s_count = defaultdict(int)
        for ch in s:
            s_count[ch] += 1
        odd_count = 0
        for k in s_count:
            if s_count[k] % 2 == 1:
                odd_count += 1
                if odd_count > 1:
                    return False
        return True
        