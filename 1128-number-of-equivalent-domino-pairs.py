class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = [0 for i in range(45)]
        for domino in dominoes:
            a = min(domino[0], domino[1])
            b = max(domino[0], domino[1])
            idx = (20 - a) * (a - 1) // 2 + b - a
            counts[idx] += 1
        
        result = 0
        for count in counts:
            if count >= 2:
                result += count * (count - 1) // 2
        return result