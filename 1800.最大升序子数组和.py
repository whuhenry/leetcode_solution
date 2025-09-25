#
# @lc app=leetcode.cn id=1800 lang=python3
#
# [1800] 最大升序子数组和
#

# @lc code=start
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        head = 0
        tail = 0
        re = 0
        l = len(nums)
        sum_ele = 0
        while head < l and tail < l:
            sum_ele += nums[tail]
            tail += 1
            if tail < l and nums[tail] <= nums[tail - 1]:
                head = tail
                re = max(re, sum_ele)
                sum_ele = 0
        re = max(re, sum_ele)
        return re
        
# @lc code=end

