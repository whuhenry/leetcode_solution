class Solution:
    def waysToStep(self, n: int) -> int:
        n3, n2, n1 = 0
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 4
        else:
            for i in range(4, n + 1):
                cur = n3 + n2 + n1
                n1, n2, n3 = cur, n1, n2
            return cur