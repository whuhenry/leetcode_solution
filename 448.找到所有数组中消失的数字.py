#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

from typing import List

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = 1
        result = []
        for val in nums:
            if val != n:
                for i in range(n, val):
                    result.append(i)
            n = val + 1
        for i in range(n, len(nums) + 1):
            result.append(i)
        return result
            
# @lc code=end

