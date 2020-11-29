#
# @lc app=leetcode.cn id=268 lang=python3
#
# [268] 丢失的数字
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for val in nums:
            sum += val
        n = len(nums)
        return n * (n + 1) // 2 - sum
# @lc code=end

