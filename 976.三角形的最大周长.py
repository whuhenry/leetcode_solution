#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 三角形的最大周长
#

from typing import List

# @lc code=start
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        result = 0
        count = len(A)
        A.sort(reverse = True)
        for i in range(count - 2):
            a = A[i]
            if a * 3 <= result:
                break
            for j in range(i + 1, count - 1):
                b = A[j]
                if a + b * 2 <= result:
                    break
                c = A[j + 1]
                if b + c > a and a + b + c > result:
                    result = a + b + c
        return result
# @lc code=end

