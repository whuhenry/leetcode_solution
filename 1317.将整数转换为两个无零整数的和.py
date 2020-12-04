#
# @lc app=leetcode.cn id=1317 lang=python3
#
# [1317] 将整数转换为两个无零整数的和
#

from typing import List

# @lc code=start
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        sep = []
        while n > 0:
            sep.append(n % 10)
            n = n // 10
        for i in range(len(sep) - 1):
            if sep[i] <= 1:
                sep[i] += 10
                sep[i + 1] -= 1
        if sep[-1] == 0:
            sep.pop()
        
        result = [0, 0]
        for num in sep[::-1]:
            tmp = num // 2
            result[0] = tmp + result[0] * 10
            result[1] = num - tmp + result[1] * 10
        return result
        

        
# @lc code=end

s = Solution()
print(s.getNoZeroIntegers(10000))