import math

class Solution:
    def paintingPlan(self, n: int, k: int) -> int:
        def comb(n,m):
            return math.factorial(n)//(math.factorial(n-m)*math.factorial(m))

        if k == n * n:
            return 1

        result = 0
        for p in range(n):
            if p * n > k:
                break
            base_p = comb(n, p)
            for q in range(n):
                cell = (p + q) * n - p * q
                if cell > k:
                    break
                if cell == k:
                    result += base_p * comb(n, q)
                    break
        
        return result

s = Solution()
print(s.paintingPlan(2, 4))