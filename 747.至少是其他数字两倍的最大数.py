#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

from typing import List

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        big1, big2 = -1, -1
        idx1, idx2 = -1, -1
        for i, num in enumerate(nums):
            if num > big1:
                big2 = big1
                big1 = num
                idx1 = i
            elif num > big2:
                big2 = num
                idx2 = i
        if big1 >= big2 * 2:
            return idx1
        return -1
        
# @lc code=end

s = Solution()
s.dominantIndex([1, 2, 3, 4])