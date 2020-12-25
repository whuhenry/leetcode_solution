import bisect

class Solution:
    def breakfastNumber(self, staple: List[int], drinks: List[int], x: int) -> int:
        staple.sort()
        drinks.sort()
        min_d = drinks[0]
        idx_d = len(drinks) - 1
        result = 0
        for s in staple:
            if s + min_d > x:
                break
            while s + drinks[idx_d] > x:
                idx_d -= 1
            result += idx_d + 1
            result = result % 1000000007
        return result