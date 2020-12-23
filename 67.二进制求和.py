#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na, nb = len(a), len(b)
        nr = max(na. nb)
        result = [0] * nr
        
        
        for i in range(na):
            result[i] += a[na - i - 1]

        for i in range(nb):
            result[i] += b[nb - i - 1]
        
        for i in range(nr - 1):
            result[i + 1] += result[i] >> 1
            result[i] = result[i] % 2
        
        while result[-1] > 1:
            result.append(result[-1] >> 1)
            result[-2] = result[-2] % 2
        return ''.join(result[::-1])
        


# @lc code=end

