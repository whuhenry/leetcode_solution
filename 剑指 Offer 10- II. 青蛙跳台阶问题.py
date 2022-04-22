class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        pre = 1
        prepre = 1
        for i in range(2, n + 1):
            cur = (pre + prepre) % 1000000007
            prepre = pre
            pre = cur
        return pre
