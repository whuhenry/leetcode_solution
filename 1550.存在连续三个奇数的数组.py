#
# @lc app=leetcode.cn id=1550 lang=python3
#
# [1550] 存在连续三个奇数的数组
#

from typing import List

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:      
        pre_odd = 0
        for num in arr:
            if num % 2 == 1:
                pre_odd += 1
                if pre_odd >= 3:
                    return True
            else:
                pre_odd = 0
        return False

# @lc code=end

