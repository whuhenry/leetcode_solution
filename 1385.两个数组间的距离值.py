#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

from typing import List

# @lc code=start
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for a1 in arr1:
            flag = True
            for a2 in arr2:
                if abs(a2 - a1) <= d:
                    flag = False
                    break
            if flag:
                result += 1
        return result
            
# @lc code=end

