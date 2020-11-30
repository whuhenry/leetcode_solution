#
# @lc app=leetcode.cn id=628 lang=python3
#
# [628] 三个数的最大乘积
#

from typing import List

# @lc code=start
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums_pos = []
        nums_neg = []
        for num in nums:
            if num >= 0:
                nums_pos.append(num)
            else:
                nums_neg.append(num)
        nums_pos.sort(reverse=True)
        nums_neg.sort()
        
        result = nums[0] * nums[1] * nums[2]
        if len(nums_pos) >= 3:
            result = max(result, nums_pos[0] * nums_pos[1] * nums_pos[2])
        if len(nums_pos) >= 1 and len(nums_neg) >= 2:
            result = max(result, nums_pos[0] * nums_neg[0] * nums_neg[1])
        if len(nums_pos) >= 2 and len(nums_neg) >= 1:
            result = max(result, nums_pos[-1] * nums_pos[-2] * nums_neg[-1])
        if len(nums_neg) >= 3:
            result = max(result, nums_neg[-3] * nums_neg[-2] * nums_neg[-1])
        return result

# @lc code=end

